from deepface import DeepFace
import pandas as pd
import base64
from django.conf import settings


class Facecall():
    def face_authenticate(self , imageBase):  

        data = imageBase

        facematch =  False
        imgdata = base64.b64decode(data)
        filename = "{}temp.jpg".format(settings.MEDIA_ROOT)
        # filename = 'promise.jpg'  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)
            

        df = DeepFace.find(img_path = settings.MEDIA_ROOT+'img1.jpg', db_path = settings.MEDIA_ROOT+'sets')

        if df.shape[0] > 0 :
            matched  = df.iloc[0].identity
            print(matched)
            facematch = True
        else:
            print("no match")
        
        return facematch

