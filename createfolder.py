# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 21:31:29 2022

@author: ACER
"""
import os
import os.path
import shutil
import cv2

raw_path='C:/Users/ASUS/Downloads/DATASET DTS/test_v2_raw/'
cleaned_path ='C:/Users/ASUS/Downloads/DATASET DTS/test_v2_clean/'


def readfilename(jalur):
    os.chdir(jalur)
    list_file=[]
    x=0
    #print ("Masuk 2")
    # iterate through all file
    for file in os.listdir():
        file_path = f"{jalur}\{file}"
        #print ("masuk")
        temp = file_path
        temp2 = os.path.basename(temp)
        #temp2 = path_awal + os.path.basename(temp)+'/'
        #list_file.append(cv2.imread(os.path.join(base_path9, temp2)))
        list_file.append(temp2)
        x=x+1
    #print (list_file[:10])
    return list_file

list_form_awal = readfilename(raw_path)
#print (path)
print ("lst : ", list_form_awal)
z=0
for x in enumerate(list_form_awal):
    newpath = cleaned_path + list_form_awal[z] +'/'
    z=z+1
    print (cleaned_path)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    



#for x in range(2):
#    for y in range(10):
#        for z in range(10):
#            for a in range (10):
#                folder =  str(x) + str(y) + str(z) + str(a)
#                if folder >= nol:
#                    break
#                else: 
#                    newpath = base_path + folder
#                    print (base_path)
#                    if not os.path.exists(newpath):
#                        os.makedirs(newpath)
