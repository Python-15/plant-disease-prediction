# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:59:28 2019

@author: Aakash Kumar
"""

import json
import requests
headers = {"Authorization": "Bearer ### access token ###"}
para = {
    "name": "maxresdefault.jpg",
    "parents": ["### folder ID ###"]
}
files = {
    'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
    'file': open("D:\downloads\maxresdefault.jpg", "rb")
}
r = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=headers,
    files=files
)
print(r.text)