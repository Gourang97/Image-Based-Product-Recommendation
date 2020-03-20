import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import urllib
import requests
import time
 
df_all = df_all.iloc[XX:,:] 
 
l, i = len(df_all), 0


for file_name, file_path in zip(df_all['filename'], df_all['link']):
    file_path_to_store = "../images/" + str(file_name)   
    f = open(file_path_to_store, 'wb')
    try:
        f.write(requests.get(file_path).content)
    except:
        f.write("")
    
    f.close()
    
    print (file_name, " saved to ", file_path_to_store)
    i += 1
    
    if i % 15 == 0:
        time.sleep(2)
    print (str(i), "/", str(l))