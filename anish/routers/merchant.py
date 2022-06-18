from fastapi import APIRouter, Depends, status, HTTPException
import database, hashing, schemas, oauth2
from sqlalchemy.orm import Session
from typing import List
from repository import merchant
from models import User

router = APIRouter(
    prefix="/user",
    tags=['Users']
)


@router.get('/', response_model=List[schemas.ShowUsr])
def all(db: Session = Depends(database.get_db), current_user: schemas.UsrBase = Depends(oauth2.get_current_user)):
    return merchant.get_all(db)


# ,current_user:schemas.UsrBase=Depends(oauth2.get_current_user)
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUsr)
def create(request: schemas.UsrBase, db: Session = Depends(database.get_db)):
    return merchant.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(database.get_db),
            current_user: schemas.UsrBase = Depends(oauth2.get_current_user)):
    return merchant.destroy(id, db)


@router.get('/{id}', response_model=schemas.ShowUsr, status_code=200)
def get_user(id: int, db: Session = Depends(database.get_db),
             current_user: schemas.UsrBase = Depends(oauth2.get_current_user)):
    return merchant.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.UsrBase, db: Session = Depends(database.get_db)):
    return merchant.update(id, request, db)


