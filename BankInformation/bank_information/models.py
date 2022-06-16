from sqlalchemy import Column,Integer,String,JSON,DateTime
from bank_information.database import Base


class Bank(Base):
    __tablename__= 'merchant_bank_details'
    __table_args__ = {'extend_existing': True}

    bank_id=Column(Integer,primary_key=True)
    paynet_merchant_id=Column(Integer)
    account_number=Column(Integer)
    account_holder_name=Column(String(100))
    bank_info=Column(JSON)
    bank_stmt_url=Column(String(100))
    status=Column(Integer)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)



