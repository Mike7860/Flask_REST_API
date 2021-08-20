# General info
Project performed on venv in Python 3.9
Creating virtual environment is mandatory

# In CMD:
pip install -r requirements.txt
cd venv 
cd Scripts
activate

# Run app:
python app.py

Suggest using Postman to check that API
for example:
POST http://127.0.0.1:5000/
BODY {
        "name": "Staples Center",
        "address": "1111 S Figueroa St",
        "city": "Los Angeles",
        "state": "CA",
        "postal_code": "90015",
        "value": "high",
        "created": "{utc.datetime}"
    }

# Endpoints:
/ - list all stored addresses in db, add new address
/filtered - list filtered (value="high") addresses in db
