from pydantic import BaseModel, Field
from typing import Dict
from fastapi import FastAPI, HTTPException

app = FastAPI()


accounts_db: Dict[str, float] = {
    "525245": 1000.0,
    "525246": 2000.0,
    "353545": 500.0
}

class Account(BaseModel):
    account_number: str
    balance: float

class Transaction(BaseModel):
    source_account: str
    destination_account: str
    amount: float = Field(gt=0, description="Amount must be greater than zero")

@app.get("/accounts/{account_number}", response_model=Account)
def get_account(account_number: str):
    if account_number not in accounts_db:
        raise HTTPException(status_code=404, detail="Account not found")
    return Account(account_number=account_number, balance=accounts_db[account_number])

@app.post("/transfer/")
def transfer_funds(transaction: Transaction):
    src = transaction.source_account
    dest = transaction.destination_account
    amt = transaction.amount

    if src not in accounts_db:
         raise HTTPException(status_code=404, detail="Source account not found")
    if dest not in accounts_db:
        raise HTTPException(status_code=404, detail="Destination account not found")
    if accounts_db[src] < amt:
       raise HTTPException(status_code=400, detail="Insufficient funds")

    
    accounts_db[src] -= amt
    accounts_db[dest] += amt

    return {"message": "Transfer successful", "new_balance": accounts_db[src]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
