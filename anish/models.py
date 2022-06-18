from sqlalchemy import Column,Integer,String,DateTime
from database import Base

class KYC(Base):
    __tablename__= 'kyc_det'
    __table_args__ = {'extend_existing': True}

    kyc_id=Column(Integer,primary_key=True,index=True)
    paynet_merchant_id=Column(Integer)
    aadhar_no=Column(Integer)
    aadhar_holder_name=Column(String(60))
    aadhar_url=Column(String(255))
    pan_no=Column(String(12))
    pan_holder_name=Column(String(60))
    pan_holder_url=Column(String(255))
    created_at=Column(DateTime)
    updated_at=Column(DateTime)

class User(Base):
    __tablename__='user'
    __table_args__ = {'extend_existing': True}

    user_id=Column(Integer,primary_key=True, index=True)
    first_name=Column(String(100))
    last_name=Column(String(100))
    email=Column(String(255),unique=True)
    password=Column(String(255))
    phone_number = Column(String(15))
    status = Column(Integer)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)

class Login(Base):

    __tablename__='login'
    __table_args__={'extend_existing':True}

    id=Column(Integer,primary_key=True,index=True)
    email=Column(String(255))
    password=Column(String(255))

from sqlalchemy import Column,Integer,String,JSON,DateTime
from database import Base


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

class person(Base):
    __tablename__='PersonalInformation'
    __table_args__={'extend_existing':True}

    user_id=Column(Integer,primary_key=True)
    first_name=Column(String(60))
    last_name=Column(String(60))
    date_of_birth=Column(String(10))
    email=Column(String(100))
    mobile_number=Column(String(15))

class Store(Base):
    __tablename__= 'storeInformation'
    __table_args__ = {'extend_existing': True}

    store_id=Column(Integer,primary_key=True)
    paynet_merchant_id=Column(Integer)
    store_name=Column(String(255))
    web_url=Column(String(255))
    store_logo_url=Column(String(255))
    address1=Column(String(100))
    address2=Column(String(100))
    city=Column(String(45))
    pincode=Column(String(6))
    state=Column(String(45))
    charge_back_no=Column(String(45))
    charge_back_email=Column(String(45))
    cust_service_no=Column(String(45))
    cust_service_email=Column(String(45))
    gst_no=Column(String(16))
    terms_conditions_url=Column(String(255))



