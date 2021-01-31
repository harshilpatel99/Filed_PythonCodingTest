# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, Text, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata



class Payment_registry(Base):
    __tablename__ = 'payment_registry'

    uuid = Column(String(256), primary_key=True)
    credit_card_number = Column(Integer(), nullable=False)
    card_holder = Column(String(256), nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    security_code = Column(Integer())
    amount = Column(Float(precision=(8,2)))
    payment_gateway = Column(String(128))
    transaction_status = Column(String(64))



