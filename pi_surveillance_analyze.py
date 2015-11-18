__author__ = 'suquark'
import requests
import oxfordcv


def analyze(path):
    requests.get('http://127.0.0.1:8888/Refrigerator_Opened', params={'path': path})
    rl = {'face_detection': oxfordcv.face_detect(path, True, True, True, True)}
    print(rl)
    return rl

if __name__ == "__main__":
    oxfordcv.face_detect('/Users/suquark/Pictures/self.jpg', True, True, True, True)
