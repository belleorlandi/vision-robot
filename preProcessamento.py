
#Pre processamento

#Importa bibliotecas
import numpy as np
import cv2
from matplotlib import pyplot as plt

# bgr_frame = cv2.imread('./colorLeft1.jpg')
# scale_percent = 40 # percent of original size
# width = int(bgr_frame.shape[1] * scale_percent / 100)
# height = int(bgr_frame.shape[0] * scale_percent / 100)
# dim = (width, height)  
# # resize image
# bgr_frame = cv2.resize(bgr_frame, dim, interpolation = cv2.INTER_AREA)

# #Escala de cinza
# gray_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)

# #Separação das camadas
# (blue_frame, green_frame, red_frame) = cv2.split(bgr_frame)

# #RED
# diffframe_red = cv2.subtract(red_frame, green_frame)
# diffframe_red = cv2.medianBlur(diffframe_red, 3)
# T_red, bin_red = cv2.threshold(diffframe_red, 40, 255, cv2.THRESH_BINARY)


# diffframe_green = cv2.subtract(green_frame, blue_frame)
# diffframe_blue = cv2.subtract(blue_frame, gray_frame)

# fig= plt.figure(figsize=(10,7))

capL = cv2.VideoCapture(2)

# Reading the mapping values for stereo image rectification
cv_file = cv2.FileStorage("improved_params2.xml", cv2.FILE_STORAGE_READ)
Left_Stereo_Map_x = cv_file.getNode("Left_Stereo_Map_x").mat()
Left_Stereo_Map_y = cv_file.getNode("Left_Stereo_Map_y").mat()
Right_Stereo_Map_x = cv_file.getNode("Right_Stereo_Map_x").mat()
Right_Stereo_Map_y = cv_file.getNode("Right_Stereo_Map_y").mat()
cv_file.release()

while True:

    # Captura de frames
    s, bgr_frame = capL.read()
    bgr_frame= cv2.remap(bgr_frame,
                        Left_Stereo_Map_x,
                        Left_Stereo_Map_y,
                        cv2.INTER_LANCZOS4,
                        cv2.BORDER_CONSTANT,
                        0)
    # bgr_frame = np.rot90(bgr_frame)
    gray_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)
    (blue_frame, green_frame, red_frame) = cv2.split(bgr_frame)
    subframe_red = cv2.subtract(red_frame, green_frame)
    diffframe_red = cv2.subtract(red_frame, green_frame)
    diffframe_red = cv2.medianBlur(diffframe_red, 3)
    T_red, bin_red = cv2.threshold(diffframe_red, 40, 255, cv2.THRESH_BINARY)
    cv2.imshow('Original', bgr_frame)
    cv2.imshow('Resultado', bin_red)

	# diffframe_green = cv2.subtract(green_frame, blue_frame)
	# diffframe_blue = cv2.subtract(blue_frame, gray_frame)
	# cv2.imshow('Original', bgr_frame)
	# cv2.imshow('Escala de cinza', gray_frame)
	#cv2.imshow('Camada RED', T_red)
	# cv2.imshow('Camada BLUE', blue_frame)
	# cv2.imshow('Camada GREEN', green_frame)

    plt.subplot(2,2,1), plt.imshow(cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2RGB)),plt.title("Original"), plt.xticks([]), plt.yticks([])
	
	# plt.subplot(1,2,2), plt.imshow(red_frame, 'gray'),plt.title("Escala de cinza"), plt.xticks([]), plt.yticks([])

	# plt.subplot(2,2,2), plt.imshow(cv2.cvtColor(subframe_red, cv2.COLOR_BGR2RGB)),plt.title("Camada Vermelha"), plt.xticks([]), plt.yticks([])
	# plt.subplot(2,2,3), plt.imshow(cv2.cvtColor(blue_frame, cv2.COLOR_BGR2RGB)),plt.title("Camada Azul"), plt.xticks([]), plt.yticks([])
	# plt.subplot(2,2,4), plt.imshow(cv2.cvtColor(green_frame, cv2.COLOR_BGR2RGB)),plt.title("Camada Verde"), plt.xticks([]), plt.yticks([])
	
	# plt.subplot(2,2,2), plt.imshow(diffframe_red, 'gray'),plt.title("Camada Vermelha"), plt.xticks([]), plt.yticks([])
	# plt.subplot(2,2,3), plt.imshow(cv2.cvtColor(diffframe_blue, cv2.COLOR_BGR2RGB)),plt.title("Camada Azul"), plt.xticks([]), plt.yticks([])
	# plt.subplot(2,2,4), plt.imshow(cv2.cvtColor(diffframe_green, cv2.COLOR_BGR2RGB)),plt.title("Camada Verde"), plt.xticks([]), plt.yticks([])

    plt.subplot(2,2,2), plt.imshow(subframe_red, 'gray'),plt.title("Subtraido"), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3), plt.imshow(diffframe_red, 'gray'),plt.title("Filtrado"), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4), plt.imshow(bin_red, 'binary'),plt.title("Binario"), plt.xticks([]), plt.yticks([])

    M = cv2.moments(bin_red)
    if M['m00'] > 0:
    	cX = int(M['m10']/M['m00'])
    	cY = int(M['m01']/M['m00'])
    	print("centroide:{} {}".format(cX, cY))
    else:
    	print('Objeto nao encontrado')
       #Exibe os frames resultantes - interrompe processo com 'q'
    #cv2.imshow('Inicio', bgr_frame)
    # cv2.imshow('Resultado', bin_red)
    #cv2.imshow("Image", bin_blue)

    # plt.show()
    if cv2.waitKey(1) == 27:
    	cv2.destroyAllWindows()
    	break

