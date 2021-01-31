import unittest
from app import app, init_app

post_param = {
    "CreditCardNumber": "9876 5412 5879 1234",
    "CardHolder": "Test Harshil",
    "ExpirationDate": "2025-12-25",
    "SecurityCode": "123",
    "Amount": 1000
}

class TestCreateSuccess(unittest.TestCase):
    def setUp(self):
        init_app(app)
        self.app = app.test_client()

    def test_get(self):
        response = self.app.post('/process_payment', json=post_param)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
