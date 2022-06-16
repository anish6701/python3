from fastapi import FastAPI,UploadFile,File
import base64
from typing import List

# Convert image to string

app=FastAPI()

@app.post('/img')
def upload_image(file:List[UploadFile]=File(...)):
    for img in file:
        with open(f"{img.filename}","rb") as image2string:
            converted_string=base64.b64encode(image2string.read())
        print(converted_string)

        with open('encode.bin',"wb") as file:
            file.write(converted_string)

# Convert String to image

        file=open('encode.bin',"rb")
        byte=file.read()
        file.close()

        decodeit=open(f'anish4.png','wb')
        decodeit.write(base64.b64decode(byte))
        decodeit.close()

        return {"file_name":img.filename}

