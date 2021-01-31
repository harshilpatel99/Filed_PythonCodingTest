from exception.app_exception import InvalidDataException, ServerException, MissingFieldException
import re
import datetime

class Individual_Validation:
    def is_valid_credit_card_number(self, card_number):
        # Should be digit and length exactly equals to 16
        exclude_characters = ['-','.']
        for character in exclude_characters:
            card_number = card_number.replace(character,'')
        card_number = ''.join(card_number.split())
        if card_number.isdigit() and len(card_number) == 16:
            return card_number
        else:
            return False


    def is_valid_card_holder(self, card_holder):
        # Validation of card holder name with the card number from the original database must be done here.
        # As original database is not provided, I am just checking if its not null
        if card_holder:
            return True
        else:
            return False

    def is_valid_expiration_date(self, expiration_date):
        # Date is YYYY-MM-DD format
        if expiration_date:
            current_date = datetime.datetime.now()
            expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d")      

            if expiration_date > current_date:
                return True
            else:
                return False
        else:
            return False

    def is_valid_security_code(self, security_code):
        # Security code can be null or if present it should be exact of length 3
        if (security_code.isdigit() and len(security_code) == 3) or len(security_code) == 0:
            return True
        else:
            return False

    def is_valid_amount(self, amount):
        # Amount should be positive
        if amount > 0:
            return True
        else:
            return False

class Validation:
    def validate_data(self, data):
        valid_data = dict()
        individual_validation = Individual_Validation()
        if data['CreditCardNumber']:
            for_card_number = individual_validation.is_valid_credit_card_number(data['CreditCardNumber'])         # Getting cleaned card number
            if for_card_number:     
                credit_card_number = True
                valid_data['credit_card_number'] = for_card_number
            else:
                raise InvalidDataException("Invalid credit card number supplied. It should be exact 16 digit value")
        else:
            raise MissingFieldException("Credit Card Number")
        
        if data['CardHolder']:  
            if individual_validation.is_valid_card_holder(data['CardHolder']):                                    
                card_holder = data['CardHolder']
                valid_data['card_holder'] = data['CardHolder']
            else:
                raise InvalidDataException("Invalid Card Holder name")
        else:
            raise MissingFieldException("Card holder")
        
        if data['ExpirationDate']:
            if individual_validation.is_valid_expiration_date(data['ExpirationDate']):
                expiration_date = data['ExpirationDate']
                valid_data['expiration_date'] = data['ExpirationDate']
            else:
                raise InvalidDataException("Date Expired")
        else:
            raise MissingFieldException("ExpirationDate")

        if data['Amount']:
            if individual_validation.is_valid_amount(data['Amount']):
                amount = data['Amount']
                valid_data['amount'] = data['Amount']
            else:
                raise InvalidDataException("Invalid amount value. Amount should be greater then 0")
        else:
            raise MissingFieldException("Amount")


        if individual_validation.is_valid_security_code(data['SecurityCode']):
            security_code = data['SecurityCode']
            valid_data['security_code'] = data['SecurityCode']
        else:
            raise InvalidDataException("Security code is invalid. Must be exact 3 digit value")

        if credit_card_number and card_holder and expiration_date and security_code and amount:
            return valid_data
        
        else:
            raise ServerException()