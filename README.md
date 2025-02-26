# Bank Transfer API

A simple RESTful API built with FastAPI for performing account transfers. Supports in-memory data storage and basic transaction operations.

📦 Project Structure

├── main.py              # API Implementation

├── test_main.py         # Unit Tests

├── README.md            # Project Documentation


✅ Features

Check account balances

Transfer funds between accounts

Error handling for insufficient funds and invalid accounts

Unit tests for core functionalities

🔧 Installation

Clone the repository:

git clone https://github.com/WasanaKarunasena/Bank-Transfer-API.git

cd Bank-Transfer-API


Install dependencies:

pip install fastapi uvicorn pydantic pytest

🚀 Running the API

Start the FastAPI server:

uvicorn main:app --reload

API Documentation: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

📚 API Endpoints

1️⃣ Check Account Balance

Endpoint: GET /accounts/{account_number}

curl -X 'GET' \

  'http://127.0.0.1:8000/accounts/12345' \
  
  -H 'accept: application/json'
  
Response:

{

  "account_number": "525245",
  
  "balance": 1000.0
  
}

2️⃣ Transfer Funds

Endpoint: POST /transfer/

Request Body:

json

{

  "source_account": "525245",
  
  "destination_account": "525246",
  
  "amount": 100
}

Response:

json

{

  "message": "Transfer successful",
  
  "new_balance": 900.0
  
}

🧪 Running Tests

Run the tests using pytest:


pytest test_main.py

You should see output indicating all tests passed.


📖 Project Structure Explained

main.py: Contains the FastAPI routes, data models, and core logic for transfers.

test_main.py: Unit tests to validate transfer logic and error handling.

README.md: Project documentation
