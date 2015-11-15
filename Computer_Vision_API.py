__author__ = 'suquark'

import base64
import json

import requests
import os


class OnlineOCR:
    """
    curl 'https://www.projectoxford.ai/Demo/Ocr'
     -H 'Cookie: __RequestVerificationToken=vxIdQTNJ5i1Ijfex_-QR_oOMJ1lHIs3KbwaS1dr4L-mc5D2xwG6F1JuwSoAMhtQaCy0kGwUQMu2bHg6els_aXHWj_xGvtZB41fjNSWQMibo1'
    --data '@/Users/suquark/Desktop/pic_base64.dat' --compressed
    """

    def __init__(self):
        try:
            self.client = requests.Session()
            text = self.client.get('https://www.projectoxford.ai/demo/visions').text
            sp = '<input name="__RequestVerificationToken" type="hidden" value="'
            txt = text[text.find(sp) + len(sp):]
            self.token = txt[:txt.find('"')]
            print 'Online OCR Login'
        except:
            print 'Online OCR Fail'

    def recg(self, path):
        try:
            data = base64.encodestring(open(path).read())
            r = self.client.post('https://www.projectoxford.ai/Demo/Ocr',
                                 {'Data': data, 'isUrl': 'false', 'languageCode': 'en',
                                  '__RequestVerificationToken': self.token})
            dr = json.loads(json.loads(unicode(r.text)))
            s = ''
            for lines in dr['regions']:
                for line in lines['lines']:
                    for box in line['words']:
                        s += box['text'] + ' '
                    s += '\r\n'
                s += '\r\n'
            return s
        except:
            return 'ERROR'


def vision_post(func_name, url, vi_params):
    local = os.path.exists(url)
    vision_headers = {
        'Host': 'api.projectoxford.ai',
        'Content-Type': 'application/octet-stream' if local else 'application/json',
        'Ocp-Apim-Subscription-Key': '69352367526e4294ba9386961666699b'
    }
    return requests.post('https://api.projectoxford.ai/vision/v1/' + func_name,
                     params=vi_params,
                     data=open(url).read() if local else json.dumps({"Url": url}),
                     headers=vision_headers).text


# This is fast but paid, plz use it later.
def ocr(url):
    """
    unk (AutoDetect)
    zh-Hans (ChineseSimplified)
    zh-Hant (ChineseTraditional)
    cs (Czech)
    da (Danish)
    nl (Dutch)
    en (English)
    fi (Finnish)
    fr (French)
    de (German)
    el (Greek)
    hu (Hungarian)
    it (Italian)
    Ja (Japanese)
    ko (Korean)
    nb (Norwegian)
    pl (Polish)
    pt (Portuguese,
    ru (Russian)
    es (Spanish)
    sv (Swedish)
    tr (Turkish)

    # EXAMPLE:
    a = OnlineOCR()
    print a.recg('/Users/suquark/Desktop/camera.jpeg')

    {
        "language": "en",
        "textAngle": 0.0,
        "orientation": "Up",
        "regions":
        [
            {
                "boundingBox": "5,146,508,263",
                "lines":
                [
                    {
                        "boundingBox": "159,146,178,44",
                        "words":
                        [
                            {"boundingBox": "159,146,178,44", "text": "Microsoft"}
                        ]
                    },
                    {
                        "boundingBox": "8,206,357,63",
                        "words":
                        [
                            {"boundingBox": "8,212,133,57", "text": "Hello"},
                            {"boundingBox": "182,206,183,63", "text": "01STC"}
                        ]
                    },
                    {
                        "boundingBox": "5,290,508,73",
                        "words":
                        [
                            {"boundingBox": "5,300,110,63", "text": "The"},
                            {"boundingBox": "159,293,162,63", "text": "BEST"},
                            {"boundingBox": "344,290,169,71", "text": "TEAM"}
                        ]
                    },
                    {
                        "boundingBox": "252,371,197,38",
                        "words":
                        [
                            {"boundingBox": "252,371,197,38", "text": "INTERNET"}
                        ]
                    }
                ]
            }
        ]
    }
    """
    return vision_post('ocr', url, {'language': 'unk', 'detectOrientation': 'true'})


def img_analyze(url):
    return vision_post('analyses', url, {'visualFeatures': 'All'})

"""
def thumbnail(url):
    https://api.projectoxford.ai/vision/v1/thumbnails?width={number}&height={number}&smartCropping=true
"""

print ocr('/Users/suquark/Desktop/camera.jpeg')
print(img_analyze('https://www.projectoxford.ai/images/bright/face/face-verification-photo.jpg'))
print img_analyze('/Users/suquark/Desktop/camera.jpeg')

