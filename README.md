#warning: project in FREEZE


# aiofaceapp
# Faces
# AioFaceApp

You can transform your face using AI with [Faceapp](https://www.faceapp.com/)

FaceApp is an [Android](https://play.google.com/store/apps/details?id=io.faceapp) and [iOS](https://itunes.apple.com/app/id1180884341) application.

This module is an *unofficial* wrapper to their AI system.

When I wrote this module I looked at https://github.com/reloadlife/FaceApp-py(thx)

## How to install:
	```git clone https://github.com/dark0ghost/aiofaceapp.git faceapp```
	```cd faceapp && python setup.py install```

## How to use:
import aiofaceapp
import asyncio
import aiohttp

from PIL import Image


filters = ['smile', 'smile_2', 'hot', 'old', 'young', 'female', 'male'

def task() -> None:
 s: aiohttp.ClientSession = aiohttp.ClientSession()
 f = aiofaceapp(s)
 code = await f.get_code(pathfilejpg)
 b = await f.make_img(code, filters[3])
 image = Image.open(io.BytesIO(b))
 image.save('./img/'+str(code)+str(filters[n])+'.png')
 
 
  
