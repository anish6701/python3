from sqlalchemy.orm import Session
import schemas,models
import jsonschema
from jsonschema import validate
import re,datetime
from fastapi import status,HTTPException

# HAVE TO ADD VALIDATIONS FOR NAME AND FEW OPTIONS


bank_info={
    "type":"object",
    "properties":{
        "Address":{"type":"string"},
        "City":{"type":"string"},
        "District":{"type":"string"},
        "State":{"type":"string"},
        "Branch":{"type":"string"},
        "IFSC":{"type":"string"},
    },
}

def create(request:schemas.bank,db:Session):
    h=models.Bank(paynet_merchant_id=request.paynet_merchant_id,account_number=request.account_number,
                  account_holder_name=request.account_holder_name,
                  bank_info=request.bank_info,bank_stmt_url=request.bank_stmt_url,status=request.status,created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())

    db.add(h)
    db.commit()
    db.refresh(h)
    return h

def validateJson(jsondata):
    try:
        validate(instance=jsondata,schema=bank_info)
    except jsonschema.exceptions.ValidationError:
        return False
    return True

def get_all(db:Session):
    print('hello in get_all ')
    h=db.query(models.Bank).all()
    return h

def destroy(id:int,db:Session):
    print('hello in delete ')
    h=db.query(models.Bank).filter(models.Bank.bank_id==id)
    if not h.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"bank with id {id} is not available")
    h.delete(synchronize_session=False)
    db.commit()
    return 'done'

def show(id:int,db:Session):
    print('hello in show')
    h=db.query(models.Bank).filter(models.Bank.bank_id==id).first()
    if not h:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"bank with id {id} is not available")
    return h

def update(id:int,request:schemas.bank,db:Session):
    print('hello in update ')
    h=db.query(models.Bank).filter(models.Bank.bank_id==id)
    if not h.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"bank with id {id} is not available")
    h.update(request.dict())
    db.commit()
    return 'it has been updated'