# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 12:47:24 2019

@author: Aakash Kumar
"""

import os
import pandas as pd

# get path to Google Drive local folder
google_drive_path = ‘~/Google\Drive’
 
sample_file = pd.read_csv(‘~/Downloads/sample.csv’)

# join path with file to be uploaded 
upload_path = os.path.join(google_drive_path, ‘sample_file.csv’)
 
# save file to drive 
sample_file.to_csv(upload_path) 