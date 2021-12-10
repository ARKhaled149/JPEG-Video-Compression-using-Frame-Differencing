#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
capture = cv2.VideoCapture(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\demo44.mp4')
success,image = capture.read()
count = 0
while success:
  cv2.imwrite(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\frame%d.jpg' % count, image)
  success,image = capture.read()
  print('Read a new frame: ', success)
  count += 1


# In[9]:


import cv2
import numpy as np
def get_difference(image_path_1, image_path_2):
    image1 = cv2.imread(image_path_1)
    image2 = cv2.imread(image_path_2)
    ResFrame = cv2.subtract(image1, image2)
    cv2.imwrite(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\ResidualFrames\ResFrame%d.jpg' %count2, ResFrame)
    
capture = cv2.VideoCapture(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\demo44.mp4')

success2,image2 = capture.read()    
count2 = 0
count3 = 1
while success2:
    get_difference(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\frame%d.jpg'%count3,
                   r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\frame%d.jpg'%count2)
    success2,image = capture.read()
    print('Read a new frame: ', success2)
    count2 += 1
    count3 += 1


# In[10]:


import cv2 as cv
ResFrame5 = cv.imread(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\ResidualFrames\ResFrame5.jpg')
cv.imshow("ResFrame5",ResFrame5)
ResFrame10 = cv.imread(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\ResidualFrames\ResFrame10.jpg')
cv.imshow("ResFrame10",ResFrame10)

img0 = cv.imread(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\frame0.jpg')
cv.imwrite(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame0.jpg',img0)


# In[3]:


import numpy as np
import cv2 as cv

def get_addition(image_path_1, image_path_2):
    image1 = cv.imread(image_path_1)
    image2 = cv.imread(image_path_2)
    OrgFrame = cv.add(image1, image2)
    cv.imwrite(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame%d.jpg' %count3, OrgFrame)
    
def get_addition2(image_path_1, image_path_2):
    image1 = cv.imread(image_path_1)
    image2 = cv.imread(image_path_2)
    OrgFrame = cv.add(image1, image2)
    cv.imwrite(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame%d.jpg' %count5, OrgFrame)
       

capture = cv.VideoCapture(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\demo44.mp4')
success2,image2 = capture.read()    
count2 = 0
count3 = 1

while success2:
    get_addition(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame%d.jpg'%count2,
                 r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\ResidualFrames\ResFrame%d.jpg'%count3)
    if count2 == 14:
        count4 = 15
        count5 = 16
        img15 = cv.imread(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\frame15.jpg')
        cv.imwrite(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame15.jpg',img15)
        get_addition2(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\Orgframe15.jpg',
                      r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\ResidualFrames\ResFrame16.jpg')
    else:
        if count2 == 29:
            count4 = 30
            count5 = 31
            img30 = cv.imread(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\frame30.jpg')
            cv.imwrite(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame30.jpg',img30)
            get_addition2(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\Orgframe30.jpg',
                          r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\ResidualFrames\ResFrame31.jpg')
        else:
            if count2 == 44:
                count4 = 45
                count5 = 46
                img45 = cv.imread(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\frame45.jpg')
                cv.imwrite(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame45.jpg',img45)
                get_addition2(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\Orgframe45.jpg',
                              r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\ResidualFrames\ResFrame46.jpg')
            else:
                if count2 == 59:
                    count4 = 60
                    count5 = 61
                    img60 = cv.imread(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\frame60.jpg')
                    cv.imwrite(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame60.jpg',img60)
                    get_addition2(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\Orgframe60.jpg',
                                  r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\ResidualFrames\ResFrame61.jpg')
    success2,image = capture.read()
    print('Read a new frame: ', success2)
    count2 += 1
    count3 += 1


# In[4]:


import numpy as np
import cv2 as cv
import glob

OrgFrame5 = cv.imread(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame5.jpg')
cv.imshow("OrgFrame5",OrgFrame5)
OrgFrame10 = cv.imread(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\OrgFrame10.jpg')
cv.imshow("OrgFrame10",OrgFrame10)

img_array = []
for filename in glob.glob(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\OriginalFrames\*.jpg'):
    img = cv.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv.VideoWriter(r'D:\User Documents\Downloads\Video and Audio Technology\Practical\Assignment1\AssignmentVideo.avi',cv.VideoWriter_fourcc(*'DIVX'), 15, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


# In[ ]:




