#Grab 2 pictures, left and right

#importacao da biblioteca numpy (computacao cientifica, manipulacao de arrays e algebra linear)
import numpy as np 
# importacao da biblioteca OpenCV (Open Source Computer Vision Library)
import cv2 as cv

#capL = cv.VideoCapture(1) # cria um objeto de captura de video utilizando a camera padrao. 
capR = cv.VideoCapture(2) # cria um objeto de captura de video utilizando a camera padrao.

#Captura a imagem e salva em disco
while(capR.isOpened()):
	# retL, frameL = capL.read() 
	# frameL = np.rot90(frameL)
	# cv.imshow('frame', frameL) # exibe imagem 	
	retR, frameR = capR.read() 
	frameR = np.rot90(frameR)
	cv.imshow('frame', frameR) # exibe imagem 				
	if cv.waitKey(1) & 0xFF == ord('s'):
		# cv.imwrite('colorLeft1_jpg.jpg', frameL) # salva a imagem em 'jpg'
		cv.imwrite('colorRight1_jpg.jpg', frameR) # salva a imagem em 'jpg'
		break
cv.destroyAllWindows()