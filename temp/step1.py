#STEP 1: identifica o centroide da bolinha
#Cor ainda nao ajustavel durante execução
#Precisa transformar a resposta do centroide em retorno de funcao

#Pre processamento

#Importa bibliotecas
import numpy as np
import cv2


def preProcessing(bgr_frame):
    bgr_frame = cv2.flip(bgr_frame, 1)

    gray_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)
    (blue_frame, green_frame, red_frame) = cv2.split(bgr_frame)
    
    diffframe_red = cv2.subtract(red_frame, gray_frame)
    diffframe_red = cv2.medianBlur(diffframe_red, 3)
    T_red, bin_red = cv2.threshold(diffframe_red, 40, 255, cv2.THRESH_BINARY)
   
    diffframe_green = cv2.subtract(green_frame, blue_frame)
    diffframe_green = cv2.medianBlur(diffframe_green, 3)
    T_green, bin_green = cv2.threshold(diffframe_green, 40, 255, cv2.THRESH_BINARY)
   
    diffframe_blue = cv2.subtract(blue_frame, gray_frame)
    diffframe_blue = cv2.medianBlur(diffframe_blue, 3)
    T_blue, bin_blue = cv2.threshold(diffframe_blue, 20, 255, cv2.THRESH_BINARY)

    return	bin_blue, bin_green, bin_red


webcam = cv2.VideoCapture(1) #inicia objeto da camera 
webcam.set(3,400)
webcam.set(4,600)

while(True):
    # Captura de frames
    s, bgr_frame = webcam.read()
    bgr_frame = np.rot90(bgr_frame)

    #Pre processmento
    bin_blue, bin_green, bin_red = preProcessing(bgr_frame)    
    selectedFrame = bin_red #COR SELECIONADA
    selectedFrame = cv2.erode(selectedFrame, None, iterations=4)
    selectedFrame = cv2.dilate(selectedFrame, None, iterations=3)
    

    # params = cv2.SimpleBlobDetector()
    # # Filter by Area.
    # params.filterByArea = False
    # params.minArea = 1500
    # # Filter by Circularity
    # params.filterByCircularity = False
    # params.minCircularity = 0.1
    # # Filter by Convexity
    # params.filterByConvexity = False
    # params.minConvexity = 0.87
    # detector = cv2.SimpleBlobDetector()
    # print('test1')
    # keypoints = detector.detect(selectedFrame) # Detect blobs.
    # print('test2')
    # print(keypoints)
    # im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # cv2.imshow("Keypoints", im_with_keypoints)

    M = cv2.moments(selectedFrame)
    if M['m00'] > 0:
    	cX = int(M['m10']/M['m00'])
    	cY = int(M['m01']/M['m00'])
    #cv2.circle(selectedFrame, (cX, cY), 10, (0, 0, 255), -1)
    #cv2.putText(bin_blue, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
    	print("centroide: {} {}".format(cX, cY))

    else:
    	print('Objeto nao encontrado')
       #Exibe os frames resultantes - interrompe processo com 'q'
    #cv2.imshow('Inicio', bgr_frame)
    cv2.imshow('Resultado', selectedFrame)
    #cv2.imshow("Image", bin_blue)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Encerrando processo
webcam.release() # Dispensa o uso da webcam
cv2.destroyAllWindows() # Fecha todas a janelas abertas