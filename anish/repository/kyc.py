import datetime
import re
from sqlalchemy.orm import Session
import schemas,models
import base64
import os
from fastapi import HTTPException,status

def validateKyc(request):
    regex_name = '[@_!#$%^&*()<>?\/\\|}{~:]'
    regex_aadhar_no = re.compile("^[2-9]{1}[0-9]{3}"+
                                 "[0-9]{4}[0-9]{4}$")
    regex_pan_no = re.compile("[A-Z]{5}[0-9]{4}[A-Z]{1}")
    a=re.compile(regex_aadhar_no)
    p=re.compile(regex_pan_no)

    if(bool(re.search(regex_name,request.aadhar_holder_name))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid name on aadhar')

    if(bool(re.search(regex_name,request.pan_holder_name))):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid name on pan')

    if(bool(re.match(a,request.aadhar_no))):
        return "valid aadhar no"
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid aadhar no')

    if(bool(re.match(p,request.pan_no))):
        return "valid pan number"
    else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Invalid pan no')


def create(request:schemas.pan,db:Session):
    validateKyc(request)
    print("inside create")
    kyc=models.KYC(paynet_merchant_id=request.paynet_merchant_id,
                   aadhar_no=request.aadhar_no,
                   aadhar_holder_name=request.aadhar_holder_name,aadhar_url=aadhar(request),
                   pan_no=request.pan_no,pan_holder_name=request.pan_holder_name,
                   pan_holder_url=pan(request),created_at=datetime.datetime.now(),updated_at=datetime.datetime.now())

    db.add(kyc)
    db.commit()
    db.refresh(kyc)
    return kyc

def pan(request):
    image2=request.image2
    mid=request.paynet_merchant_id
    directory = os.getcwd()
    print(directory)
    filepath = os.getcwd() + "/" + f"PAN_MID_" + str(mid) + ".jpeg"
    decodeit = open(filepath, 'wb')
    decodeit.write(base64.b64decode(image2 + str(b'==')))
    decodeit.close()
    return filepath


def aadhar(request):
    image1= request.image1
    mid=request.paynet_merchant_id
    directory = os.getcwd()
    print(directory)
    filepath = os.getcwd() + "/" + f"AADHAR_MID_"+str(mid) +".jpeg"
    print(filepath)
    decodeit = open(filepath, 'wb')
    # decodeit = open(f'pan.jpeg', 'wb')
    decodeit.write(base64.b64decode(image1 + str(b'==')))
    decodeit.close()
    return filepath

def get_all(db:Session):
    kyc=db.query(models.KYC).all()
    return kyc

def destroy(id:int,db:Session):
    kyc=db.query(models.KYC).filter(models.KYC.kyc_id == id)
    if not kyc.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} is not there')
    kyc.delete(synchronize_session=False)
    db.commit()
    return f'user with id {id} deleted'

def show(id:int,db:Session):
    print('in show')
    kyc=db.query(models.KYC).filter(models.KYC.kyc_id == id).first()
    if not kyc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} is not there')
    return kyc

def update(id:int,request:schemas.updateKYC,db:Session):
    validateKyc(request)
    kyc=db.query(models.KYC).filter(models.KYC.kyc_id == id)
    pan(request)
    if not kyc.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} is not there')


    print('aadhar url', aadhar(request))
    print('pan url', pan(request))

    kyc.aadhar_url = aadhar(request)
    kyc.pan_holder_url = pan(request)

    updatesql = "update kyc_det set aadhar_no='"+request.aadhar_no+"',aadhar_holder_name='"+request.aadhar_holder_name+"'," \
                 "aadhar_url='"+kyc.aadhar_url+"', pan_no='"+request.pan_no+"',pan_holder_name='"+request.aadhar_holder_name+"'," \
                  "pan_holder_url='"+kyc.pan_holder_url+"' where kyc_id="+str(id)

    print(updatesql)
    # exit()
    db.commit()
    return "update"





