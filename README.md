## Structure

```
├── install.sh                   # Install the python env.
├── app.py                       # Application entry point
├── unit_test_transaction.py     # Unit test file
├── dal                      
│   ├── db.py                    # Defining database
│   └── model.py                 # Flask model
├── exception
│   └── app_exception.py         # All the exceptions are defined here
├── sql                          # SQL statements to create database, tables and to perform CRUD operations
├── test
│   └── postman                  # postman tests
├── transaction                      
│   ├── data_validation.py       # Validates all incoming data
│   ├── process_transaction.py   # Major entry point for transaction request
│   └── transaction_gateway      # Determines type of transaction gateway

```

## Database Creation

For database creation import init.sql and create_tables.sql to your phpmyadmin or mysql

## How to run application

Run application as follows:
    └── python app.py

## Postman Test and Unit Test

I have included both Postman test and unit test.

For postman test, I have saved it as a collection, so you can directly import it and test it.

For unit test run:
    └── python unit_test_transaction.py