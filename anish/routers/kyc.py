from typing import List
from fastapi import APIRouter,Depends,status,File,UploadFile
import schemas,database
from repository import kyc
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/kyc",
    tags=['kyc']
)

@router.get('/',response_model=List[schemas.showp])
def all(db:Session=Depends(database.get_db)):
    return kyc.get_all(db)

@router.post('/',status_code=200)
def create(request:schemas.pan,db:Session=Depends(database.get_db)):
    return kyc.create(request,db)

@router.delete('/',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session=Depends(database.get_db)):
    return kyc.destroy(id,db)

@router.get('/{id}',status_code=200,response_model=schemas.showp)
def get_user(id:int,db:Session=Depends(database.get_db)):
    return kyc.show(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.updateKYC,db:Session=Depends(database.get_db)):
    return kyc.update(id, request, db)

@router.post('/file',status_code=200)
def upload_image(file:UploadFile=File(...)):
    print('inside upload image')
    return {"name_of_file":file.filename}