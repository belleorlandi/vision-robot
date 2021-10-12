#importacao da biblioteca numpy (computacao cientifica, manipulacao de arrays e algebra linear)
import numpy as np 
# importacao da biblioteca OpenCV (Open Source Computer Vision Library)
import cv2 as cv
from matplotlib import pyplot as plt
import os, os.path
import glob

def FilesNames(preName, ext):

    numFiles = len(os.listdir('./data/stereoL')) #recebe o numero de arquivos no diretorio 
    val = numFiles
    newFileName = preName + str(val) + '.' + ext
    return [newFileName, val]

capR = cv.VideoCapture(1)
capL = cv.VideoCapture(2)

while(capL.isOpened()): 
    preNameR = 'imageR';
    preNameL = 'imageL';
    ext = 'jpg';
    [newFileNameR, val] = FilesNames(preNameR, ext)
    [newFileNameL, val] = FilesNames(preNameL, ext)
    # Realiza a captura de frames da direita e esquerda
    retR, frameR = capR.read() 
    frameR = np.rot90(frameR)
    cv.imshow('CapturaR', frameR)
    retL, frameL = capL.read() 
    frameL = np.rot90(frameL)
    cv.imshow('CapturaL', frameL)
    pathR = './data/stereoR/'
    pathL = './data/stereoL/'    
    
    if cv.waitKey(1) & 0xFF == ord('s'):
        cv.imwrite(os.path.join(pathR , newFileNameR), frameR)
        cv.imwrite(os.path.join(pathL , newFileNameL), frameL)
    
    elif val == 15: #capura 15 imagens
        break

    elif cv.waitKey(1) & 0xFF == ord('q'):
        break

print("Fim da captura")
capR.release()
capL.release()
cv.destroyAllWindows()