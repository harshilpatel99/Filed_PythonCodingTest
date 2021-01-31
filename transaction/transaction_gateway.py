
from sql.insert_data import Insert_Data


class Transaction_Gateway:
    def __init__(self):
        self.insert_data = Insert_Data()

    def cheap_payment_gateway(self, data):
        status = 'SUCCESS'
        return self.insert_data.write_to_payment_registry(data['credit_card_number'], data['card_holder'], data['expiration_date'], data['security_code'], data['amount'], 'cheap_payment_gateway', status)

    def expensive_payment_gateway(self, data):
        status = 'SUCCESS'
        return self.insert_data.write_to_payment_registry(data['credit_card_number'], data['card_holder'], data['expiration_date'], data['security_code'], data['amount'], 'expensive_payment_gateway', status)

    def premium_payment_gateway(self, data):
        status = 'SUCCESS'
        return self.insert_data.write_to_payment_registry(data['credit_card_number'], data['card_holder'], data['expiration_date'], data['security_code'], data['amount'], 'premium_payment_gateway', status)
