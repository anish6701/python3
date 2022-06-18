from fastapi import APIRouter,Depends,status
import database,schemas
from sqlalchemy.orm import Session
from typing import List
from repository import store



router=APIRouter(
    prefix="/store",
    tags=['StoreInfo']
)


@router.get('/',response_model=List[schemas.StrBase])
def all(db:Session=Depends(database.get_db)):
    return store.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.StrBase,db:Session=Depends(database.get_db)):
    return store.create(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(database.get_db)):
    return store.destroy1(id,db)

@router.get('/{id}',response_model=schemas.StrBase,status_code=status.HTTP_200_OK)
def store_by_id(id:int,db:Session=Depends(database.get_db)):
    return store.show(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.StrBase,db:Session=Depends(database.get_db)):
    return store.update(id,request,db)