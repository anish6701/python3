from fastapi import status,HTTPException
from sqlalchemy.orm import Session
import schemas,models
import re


def get_all(db:Session):
    store = db.query(models.Store).all()
    return store
'''
def create(request:schemas.StrBase,db:Session):
    strDetails = models.Store(store_id=request.store_id, data_info=request.data_info)
    db.add(strDetails)
    db.commit()
    db.refresh(strDetails)
    return strDetails

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
    terms_conditions_url=Column(String(255))'''

def validate(request):
    regex_gst = "^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$"
    regex_pincode= "^[1-9]{1}[0-9]{2}\\s{0, 1}[0-9]{3}$"
    regex_email = r'\b[A - Za - z0 - 9._ % +-]+ @ [A - Za - z0 - 9. -] +\.[A - Z | a - z]{2, }\b'

    if not (re.match(regex_gst,request.gst_no)):
        print(regex_gst,request.gst_no)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid gst number')

    if(bool(re.match(regex_pincode,request.pincode))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid pincode')

    if (bool(re.search(regex_email, request.charge_back_email))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid email.')


def create(request:schemas.StrBase,db:Session):
    validate(request)
    strDetails = models.Store(paynet_merchant_id=request.paynet_merchant_id,store_name=request.store_name, web_url=request.web_url,store_logo_url=request.store_logo_url,
                              address1=request.address1,address2=request.address2,city=request.city,pincode=request.pincode,
                              state=request.state,charge_back_no=request.charge_back_no,charge_back_email=request.charge_back_email,
                              cust_service_no=request.cust_service_no,cust_service_email=request.cust_service_email,
                              gst_no=request.gst_no,terms_conditions_url=request.terms_conditions_url)
    db.add(strDetails)
    db.commit()
    db.refresh(strDetails)
    return strDetails

def destroy1(id:int,db:Session):
    strDetails=db.query(models.Store).filter(models.Store.store_id==id)
    if not strDetails.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"store with id {id} is not available ")
    strDetails.delete(synchronize_session=False)
    db.commit()
    return 'done'

def show(id:int,db:Session):
    print("hello in show")
    strId=db.query(models.Store).filter(models.Store.store_id==id).first()
    if not strId:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Store with {id} is not available')
    return strId

def update(id:int,request:schemas.StrBase,db:Session):
    validate(request)
    usr=db.query(models.Store).filter(models.Store.store_id==id)
    if not usr.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Store with {id} is not available')
    usr.update(request.dict())
    db.commit()
    return 'hello'