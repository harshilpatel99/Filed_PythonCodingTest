from sqlalchemy.exc import IntegrityError
from dal.db import Db
import uuid
from exception.app_exception import ServerException, IntegrityException
import datetime

class Populate_Tables:
    def _populate_registry_model(self, table_type, credit_card_number, card_holder, expiration_date, security_code, amount, payment_gateway, transaction_status, retry_left):
        new_uuid = str(uuid.uuid4())
        table = table_type(uuid=new_uuid)
        table.credit_card_number = credit_card_number
        table.card_holder = card_holder
        table.expiration_date = expiration_date
        table.transaction_date = datetime.datetime.now()
        table.security_code = security_code
        table.amount = amount
        table.payment_gateway = payment_gateway
        table.transaction_status = transaction_status
        table.retry_left = retry_left
        return table

class Insert_Data:
    def write_to_payment_registry(self, credit_card_number, card_holder, expiration_date, security_code, amount, payment_gateway, status, retry_left=None):
        db_instance = Db()
        registry_table = db_instance.model.Payment_registry
        sql_registry_table = Populate_Tables._populate_registry_model(self, registry_table, credit_card_number, card_holder, expiration_date, security_code, amount, payment_gateway, status, retry_left)
        session = db_instance.session
        try:
            session.add(sql_registry_table)
            session.commit()
            if sql_registry_table.transaction_status == "SUCCESS":
                return "Payment is successful", 200
            else:
                return "Payment failed", 400

        except IntegrityError as ex:
            print(str(ex))
            session.rollback()
            raise IntegrityException(str(ex))
        
        except Exception as ex:
            print(str(ex))
            session.rollback()
            raise ServerException(str(ex))
