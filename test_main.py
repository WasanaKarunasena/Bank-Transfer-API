from fastapi.testclient import TestClient
from main import app, accounts_db

client = TestClient(app)

def test_transfer_success():
    # Reset accounts for testing
    accounts_db["525245"] = 1000.0
    accounts_db["525246"] = 2000.0
    accounts_db["353545"] = 500.0

    response = client.post("/transfer/", json={
        "source_account": "525245",
        "destination_account": "353545",
        "amount": 100
    })

    assert response.status_code == 200
    assert response.json()["message"] == "Transfer successful"
    assert accounts_db["525245"] == 900.0
    assert accounts_db["353545"] == 600.0

def test_transfer_insufficient_funds():
    response = client.post("/transfer/", json={
        "source_account": "353545",
        "destination_account": "525245",
        "amount": 1000
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient funds"

def test_transfer_invalid_account():
    response = client.post("/transfer/", json={
        "source_account": "00000",
        "destination_account": "525245",
        "amount": 100
    })
    assert response.status_code == 404
    assert response.json()["detail"] == "Source account not found"
