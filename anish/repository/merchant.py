from sqlalchemy.orm import Session
import models,schemas,hashing
from fastapi import HTTPException,status
from database import engine
import re,datetime


# Creating a user and requesting the following details
def create(request:schemas.UsrBase,db:Session):
    validatePersonal(request)
    Lst_of_users = models.User(first_name=request.first_name, last_name=request.last_name,
                                email=request.email, password=hashing.Hash.bcrypt(request.password),
                               phone_number=request.phone_number,status=request.status,created_at=datetime.datetime.utcnow())

    db.add(Lst_of_users)
    db.commit()
    usersql=engine.execute('select user_id from user order by user_id desc')
    uid = usersql.fetchone()[0]
    print(uid)
    loginsql = engine.execute("insert into login values("+str(uid)+",'"+request.email+"','"+hashing.Hash.bcrypt(request.password)+"')")
    print(loginsql)
    a='0'
    b='1'
    mersql=engine.execute("insert into merchant values("+str(uid)+","+str(uid)+","+a+","+a+","+a+","+a+","+a+","+b+",'"+str(datetime.datetime.utcnow())+"','"+str(datetime.datetime.now())+"')")
    print(mersql)
    db.commit()
    db.refresh(Lst_of_users)
    return Lst_of_users

def validatePersonal(request):
    regex_name = '[@_!#$%^&*()<>?\/\\|}{~:]'  # regular expression to check any special characters in full name and store name
    regex_email = r'\b[A - Za - z0 - 9._ % +-]+ @ [A - Za - z0 - 9. -] +\.[A - Z | a - z]{2, }\b'
    pattern = re.compile("(0|91)?[-\s]?[6-9][0-9]{9}")

    # print(regex_name,request.full_name)
    if (bool(re.search(regex_name, request.first_name))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid firstname. No special charcters allowed')

    if (bool(re.search(regex_name, request.last_name))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid lastname. No special charcters allowed')

    # print(regex_email,request.email)
    if (bool(re.search(regex_email, request.email))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid email.')

    if (pattern.match(request.phone_number)):
        print(f'{request.phone_number} is a valid number')
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f" {request.mobile_number} Invalid number.")


# deleting a user from the database
def destroy(id:int,db:Session):
    usr = db.query(models.User).filter(models.User.user_id == id)
    if not usr.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available ")
    usr.delete(synchronize_session=False)
    db.commit()
    return 'done'

# showing a specific user with the help of {id}
def show(id:int,db:Session):
    user=db.query(models.User).filter(models.User.user_id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} is not available ')
    return user

# Showing all the users from the db
def get_all(db:Session):
    user=db.query(models.User).all()
    return user

# Updating the user details which they would like to update
def update(id:int,request:schemas.UsrBase,db:Session):
    validatePersonal(request)
    p = request.password
    request.password = hashing.Hash.bcrypt(p)
    user = db.query(models.User).filter(models.User.user_id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} is not available')
    user.update(request.dict())
    db.commit()
    # return user
    return request.dict()

