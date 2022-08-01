# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 09:19:38 2022

"""
# Import Module
import os
import os.path
import shutil
import cv2
from PIL import Image, ImageOps
#import numpy as np

image_path ='C:/Users/ASUS/Downloads/DATASET DTS/test_v2_raw/'
image_path2 ='C:/Users/ASUS/Downloads/DATASET DTS/test_v2_clean/'


def preprocessing_image(image_path,image_path2):
    image = Image.open(image_path)
    width, height = image.size
    target_w = 256
    target_h = 60
    end_w = (target_w - float(width))/2
    end_h = (target_h - float(height))/2
    
    if width >= 210:
        basewidth = 256
        wpercent = (basewidth / float(image.size[0]))
        hsize = int((float(image.size[1]) * float(wpercent)))
        if hsize >224:
            baseheight=60
            hpercent = (baseheight/float(image.size[1]))
            wsize = int(basewidth * float(hpercent))
            images = image.resize((wsize, baseheight), Image.ANTIALIAS)
            new_width = (target_w - wsize)/2
            new_height = (target_h - baseheight)/2
            result = Image.new(images.mode, (target_w, target_h), 255)
            result.paste(images, (int(new_width), int(new_height)))
            end = result
            #end = ImageOps.invert(result)
            #end = end.convert('1') 
            end.save(image_path2)
        else:
            images = image.resize((basewidth, hsize), Image.ANTIALIAS)
            new_width = (target_w - basewidth)/2
            new_height = (target_h - hsize)/2
            result = Image.new(images.mode, (target_w, target_h), 255)
            result.paste(images, (int(new_width), int(new_height)))
            end = result
            #end = ImageOps.invert(result)
            #end = end.convert('1')
            end.save(image_path2)
    else:
        result = Image.new(image.mode, (target_w, target_h), 255)
        result.paste(image, (int(end_w), int(end_h)))
        end = result
        #end = ImageOps.invert(result)
        #end = end.convert('1')
        end.save(image_path2)



### kasih komen #####



path = 'C:/Users/ASUS/Downloads/DATASET DTS/test_v2_raw/'
target_path = 'C:/Users/ASUS/Downloads/DATASET DTS/test_v2_raw/'



list_form_end=[]


# Change the directory
def readfilename(jalur):
    os.chdir(jalur)
    list_file=[]
    x=0
    
    # iterate through all file
    for file in os.listdir():
        file_path = f"{path}\{file}"
        temp = file_path
        temp2 = os.path.basename(temp)
        #temp2 = path_awal + os.path.basename(temp)+'/'
        #list_file.append(cv2.imread(os.path.join(base_path9, temp2)))
        list_file.append(temp2)
        x=x+1
    #print (list_file[:10])
    return list_file

def baca_filename(bantu):
    os.chdir(bantu)
    list_file=[]
    x=0
    
    # iterate through all file
    for file in os.listdir():
        file_path = f"{path}\{file}"
        temp = file_path
        temp2 = os.path.basename(temp)
        #temp2 = path_awal + os.path.basename(temp)+'/'
        list_file.append(temp2)
        x=x+1
    #print (list_file[:10])
    return list_file

def readfilename2 (list_form):
    z=0
    for x in enumerate(list_form):
        jalur2 = image_path + list_form[z]+'/'
        print(jalur2)
        os.chdir(jalur2)
        for file in os.listdir():
            file_path = f"{path}\{file}"
            temp = file_path
            temp2 = os.path.basename(temp)
            path_bantu1 = jalur2 + temp2
            path_bantu = image_path2 + list_form[z] + '/' + temp2
            preprocessing_image(path_bantu1,path_bantu)
        z=z+1
    #print (list_file2[:10])
    #return list_form_end
    



def readfilename3 (list_form):
    chnl3=0
    chnl=0
    z=0
    for x in enumerate(list_form):
        jalur2 = base_path + list_form[z]+'/'
        jalur10 = base_path + list_form[z]
        #print(jalur2)
        os.chdir(jalur2)
        for file in os.listdir():
            file_path = f"{path}\{file}"
            temp = file_path
            temp2 = os.path.basename(temp)
            img = cv2.imread(os.path.join(jalur10, temp2))
            panjang, lebar, channel = img.shape
            if channel == 3:
                chnl3=chnl3+1
            else:
                chnl=chnl+1
                print(chnl)
            #print ('shape : ', img.shape)
            #list_form_end.append(img)
            
            #list_form_end
            list_form_end.append(temp2)
        z=z+1
    #print (list_file2[:10])
    return chnl3,chnl

def split_filename(samples):
    for (i, file_line) in enumerate(samples):
        line_split = file_line.strip()
        line_split = line_split.split(".")
        base = line_split[0]
        part = base.split("-")
        partI= part[0]
        partII= part[1]
        name=partI+'-'+partII
        #img_path = jalur5 + partI+'/'+partI+'-'+partII
        #img_path2 = jalur5 + partI+'/'+partI+'-'+partII+'/'
        print(name)
        #filenames=readfilename2(img_path,img_path2)
        #copyfile(filenames)
        
def copyfile(test_img_paths):
    #basename_train=[]
    #basename_valid=[]
    #basename_test=[]
    temp = 0

    #get filename training
    for (x, file_line) in enumerate(test_img_paths):
      basename_test = os.path.basename(file_line)
      original = test_img_paths[temp]
      target = target_path + '/' + basename_test
      shutil.copyfile(original, target)
      temp=temp+1


def buatfolder(form):
    z=0
    for x in enumerate(form):
        newpath = target_path + form [z]
        print (newpath)
        z=z+1
        if not os.path.exists(newpath):
            os.makedirs(newpath)


subset = readfilename(image_path)
subclass = readfilename2(subset)
