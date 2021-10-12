
#importacao da biblioteca numpy (computacao cientifica, manipulacao de arrays e algebra linear)
import numpy as np 
# importacao da biblioteca OpenCV (Open Source Computer Vision Library)
import cv2 as cv
from matplotlib import pyplot as plt
import os, os.path
import glob

# Le as duas imagens
imgL = cv.imread('colorLeft_jpg.jpg',0)
imgR = cv.imread('colorRight_jpg.jpg',0)

# Objeto de mapa de disparidade
stereo = cv.StereoSGBM_create(numDisparities=32, blockSize=3)

# Mapa de diparidade
disparity = stereo.compute(imgL,imgR)

# Exibe o mapa 
plt.imshow(disparity,'gray')
plt.title('Mapa Disparidade'), plt.xticks([]), plt.yticks([])
plt.show()