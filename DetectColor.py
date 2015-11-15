#！/usr/bin/env python
#-*- coding: utf-8 -*-

import json
import picamera
import requests
import tempfile
import time

url = "https://api.projectoxford.ai/vision/v1/analyses?Color"
headers={'Ocp-Apim-Subscription-Key':"INPUT YOUR API KEY HERE"}
camera=picamera.PiCamera()
camera.video_stabilization=True
LastColor = None
while True:
    f=tempfile.NamedTemporaryFile(delete=True,suffix='.jpg',prefix='camera')
    camera.capture(f.name)
    files={'file':open(f.name,'rb')}
    r=requests.post(url,files=files, headers=headers)
    data=json.loads(r.text)
    color = data["color"]["dominantColorBackground"]
    if (color != LastColor):
        print(u"报警！");
    LastColor = color
    time.sleep(1)