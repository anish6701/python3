from fastapi import APIRouter,Depends,status,HTTPException
import database,schemas
from sqlalchemy.orm import Session
from repository import bank
from typing import List

router=APIRouter(
    prefix="/bankInfo",
    tags=['bank']
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.bank,db:Session=Depends(database.get_db)):
     isValid=bank.validateJson(request.bank_info)
     if isValid:
        return bank.create(request,db)
     else:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.get('/',response_model=List[schemas.bank])
def all(db:Session=Depends(database.get_db)):
    return bank.get_all(db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(database.get_db)):
    return bank.destroy(id,db)

@router.get('/{id}',response_model=schemas.bank,status_code=status.HTTP_200_OK)
def bank_by_id(id:int,db:Session=Depends(database.get_db)):
    return bank.show(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.bank,db:Session=Depends(database.get_db)):
    return bank.update(id,request,db)