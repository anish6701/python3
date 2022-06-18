from fastapi import status,HTTPException
from sqlalchemy.orm import Session
import schemas,models
import re

def get_all(db:Session):
    person=db.query(models.person).all()
    return person

def create(request:schemas.personalBase,db:Session):
    validatePersonal(request)
    personalDetails = models.person(first_name= request.first_name,
                                    last_name=request.last_name,
                                    date_of_birth=request.date_of_birth,
                                    email=request.email,
                                    mobile_number=request.mobile_number)
    db.add(personalDetails)
    db.commit()
    db.refresh(personalDetails)

    return personalDetails

def validatePersonal(request):
    regex_name = '[@_!#$%^&*()<>?\/\\|}{~:]' # regular expression to check any special characters in full name and store name
    regex_email=r'\b[A - Za - z0 - 9._ % +-]+ @ [A - Za - z0 - 9. -] +\.[A - Z | a - z]{2, }\b'
    pattern=re.compile("(0|91)?[-\s]?[6-9][0-9]{9}")

    #print(regex_name,request.full_name)
    if(bool(re.search(regex_name,request.first_name))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Invalid name.')

    if (bool(re.search(regex_name, request.last_name))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid name.')

    #print(regex_email,request.email)
    if(bool(re.search(regex_email,request.email))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f'Invalid email.')

    if(pattern.match(request.mobile_number)):
       print(f'{request.mobile_number} is a valid number')
    else:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f" {request.mobile_number} Invalid number.")

    # test cases are stored in TESTFORVALIDATIONS mobilenumber.py



def destroy(id:int,db:Session):
    personalDetails=db.query(models.person).filter(models.person.user_id == id)
    if not personalDetails.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Store with {id} is not available')
    personalDetails.delete(synchronize_session=False)
    db.commit()
    return personalDetails

def update(id:int,request:schemas.personalBase,db:Session):
    personalDetails=db.query(models.person).filter(models.person.user_id==id)
    if not personalDetails.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'personal details with {id} is not available')
    personalDetails.update(request.dict())
    db.commit()
    return 'hi anish how you doin'

def show(id:int,db:Session):
    personalDetails=db.query(models.person).filter(models.person.user_id==id).first()
    if not personalDetails:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'personal details with {id} is not available')
    return personalDetails
