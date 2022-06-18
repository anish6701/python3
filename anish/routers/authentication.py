from fastapi import APIRouter,Depends,HTTPException,status
import schemas,database,models,token_1
from hashing import Hash
from sqlalchemy.orm import Session


router=APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post('/')
def login(request:schemas.Login,db:Session=Depends(database.get_db)):
    user=db.query(models.Login).filter(models.Login.email == request.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid credentials')

    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Incorect Password')

    access_token=token_1.create_access_token(data={"sub":user.email})
    data = {"access_toekn":access_token, "token_type":"Bearer", "user_id":user.id}
    # return {"access_token":access_token,"user_id":user.id}
    return data

#"user_id":models.Login.id,

@router.get('/')
def all(db:Session=Depends(database.get_db)):
    user = db.query(models.Login).all()
    return user