from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class pan(BaseModel):

    paynet_merchant_id :int
    aadhar_no :str
    aadhar_holder_name :str
    image1: str
    pan_no :str
    pan_holder_name :str
    image2:str
    created_at:Optional[datetime]
    updated_at:Optional[datetime]

    class Config():
        orm_mode=True

class showp(BaseModel):
    paynet_merchant_id: int
    aadhar_no: str
    aadhar_holder_name: str
    pan_no: str
    pan_holder_name: str

    class Config():
        orm_mode=True

class updateKYC(BaseModel):
    paynet_merchant_id: int
    aadhar_no: str
    aadhar_holder_name: str
    image1: str
    pan_no: str
    pan_holder_name: str
    image2:str

    class Config():
        orm_mode=True

class UsrBase(BaseModel):

    first_name :str
    last_name :str
    email :str
    password: str
    phone_number :str
    status:int


    class Config():
        orm_mode=True

class Usr(UsrBase):
    class Config():
        orm_mode=True

class ShowUsr(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    status: int
    created_at: datetime
    updated_at: datetime

    class Config():
        orm_mode=True


class Login(BaseModel):

    email:str
    password:str

    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email: str

from pydantic import BaseModel


class bank(BaseModel):


    paynet_merchant_id:int
    account_number: int
    account_holder_name:str
    bank_info: dict={
                    "Address": '',
                    "City":'',
                    "District":'',
                    "State":'',
                    "Branch":'',
                    "IFSC":''
                     }
    bank_stmt_url:str
    status:int



    class Config():
        orm_mode=True

class personalBase(BaseModel):
    first_name:str
    last_name:str
    date_of_birth:str
    email:str
    mobile_number:str

    class Config():
        orm_mode=True

class p(personalBase):
    user_id:int
    first_name: str
    last_name:str
    date_of_birth: str
    email: str
    mobile_number: str
    class Config():
        orm_mode=True


class StrBase(BaseModel):

    store_id:int
    paynet_merchant_id:int
    store_name:str
    web_url:str
    store_logo_url:str
    address1:str
    address2:str
    city:str
    pincode:str
    state:str
    charge_back_no:str
    charge_back_email:str
    cust_service_no:str
    cust_service_email:str
    gst_no:str
    terms_conditions_url:str

    class Config():
        orm_mode=True




