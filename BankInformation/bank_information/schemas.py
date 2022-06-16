from pydantic import BaseModel


class bank(BaseModel):


    paynet_merchant_id:int
    account_number: int
    account_holder_name:str
    bank_info: dict=[{
                    "Address": '',
                    "City":'',
                    "District":'',
                    "State":'',
                    "Branch":'',
                    "IFSC":''
                     }]
    bank_stmt_url:str
    status:int



    class Config():
        orm_mode=True



