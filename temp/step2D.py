#importacao da biblioteca numpy (computacao cientifica, manipulacao de arrays e algebra linear)
import numpy as np 
# importacao da biblioteca OpenCV (Open Source Computer Vision Library)
import cv2 as cv
from matplotlib import pyplot as plt
import os, os.path
import glob

mtxR = [[845.70338279   0.         249.49779193],                                         
[  0.         846.59890132 301.07810576],
[  0.           0.           1.        ]]

mtxL = [[834.88363312   0.         261.61822075],
[  0.         837.11656098 301.61554765],
[  0.           0.           1.        ]]

capR = cv.VideoCapture(1)
capL = cv.VideoCapture(2)

sR, bgr_frameR = capR.read()
bgr_frameR = np.rot90(bgr_frameR)
# cv.imwrite('originalR.jpg', bgr_frameR)

# sL, bgr_frameL = capL.read()
# bgr_frameL = np.rot90(bgr_frameL)
# cv.imwrite('originalL.jpg', bgr_frameL)

cv.destroyAllWindows() # fecha as janelas abertas