from transaction.data_validation import Validation
from transaction.transaction_gateway import Transaction_Gateway
from exception.app_exception import ServerException

class Process_Transaction:
    def proceed_to_payment_gateway(self, valid_data):
        transaction_gateway = Transaction_Gateway()
        if valid_data['amount'] < 21:
            return transaction_gateway.cheap_payment_gateway(valid_data)

        elif valid_data['amount'] >= 21 and valid_data['amount'] <= 500:
            return transaction_gateway.expensive_payment_gateway(valid_data)

        else:
            return transaction_gateway.premium_payment_gateway(valid_data)

    def initialize_payment(self, data):
        validation = Validation()
        valid_data = validation.validate_data(data)
        if valid_data:
            return self.proceed_to_payment_gateway(valid_data) 
        else:
            raise ServerException()