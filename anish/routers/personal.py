from fastapi import APIRouter,Depends,status
import database,schemas
from sqlalchemy.orm import Session
from typing import List
from repository import personal

router=APIRouter(
    prefix="/PerosnalInformation",
    tags=['PerosnalDetails']
)

@router.get('/',response_model=List[schemas.p])
def all(db:Session=Depends(database.get_db)):
    return personal.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.personalBase,db:Session=Depends(database.get_db)):
    return personal.create(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(database.get_db)):
    return personal.destroy(id,db)

@router.get('/{id}',response_model=schemas.p,status_code=status.HTTP_200_OK)
def person(id:int,db:Session=Depends(database.get_db)):
    return personal.show(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.personalBase,db:Session=Depends(database.get_db)):
    return personal.update(id,request,db)