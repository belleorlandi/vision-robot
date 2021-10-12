#Disparity test

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


imgL = cv.imread('colorRight1_jpg.jpg',0)
imgR = cv.imread('colorLeft1_jpg.jpg',0)
stereo = cv.StereoBM_create(numDisparities=32, blockSize=5)
disparity = stereo.compute(imgL,imgR)
plt.imshow(disparity,'gray')
plt.title('Mapa Disparidade'), plt.xticks([]), plt.yticks([])
plt.show()