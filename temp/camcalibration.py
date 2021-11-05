#importacao da biblioteca numpy (computacao cientifica, manipulacao de arrays e algebra linear)
import numpy as np 
# importacao da biblioteca OpenCV (Open Source Computer Vision Library)
import cv2 as cv
from matplotlib import pyplot as plt
import os, os.path
import glob

def FilesNames(preName, ext):

    numFiles = len(os.listdir('.')) - 14 #recebe o numero de arquivos no diretorio 
    val = numFiles
    newFileName = preName + str(val) + '.' + ext
    return [newFileName, val]

cap = cv.VideoCapture(2)

while(cap.isOpened()): 
    preName = 'imageL';
    ext = 'jpg';
    [newFileName, val] = FilesNames(preName, ext)
    # Realiza a captura de frames da direita e esquerda
    ret, frame = cap.read() 
    cv.imshow('Captura', frame)
    
    if cv.waitKey(1) & 0xFF == ord('s'):
        cv.imwrite(newFileName, frame)
    
    elif val == 15: #capura 15 imagens
        break

    elif cv.waitKey(1) & 0xFF == ord('q'):
        break

print("Fim da captura")

cap.release()
cv.destroyAllWindows()

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

nRows = 6
nCols = 8
    
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((nCols*nRows,3), np.float32)
objp[:,:2] = np.mgrid[0:nCols,0:nRows].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('*.jpg')

for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    # ret, corners = cv.findChessboardCorners(gray, (nCols,\nRows), flags=cv.CV_CALIB_FIX_PRINCIPAL_POINT)

    ret, corners = cv.findChessboardCorners(gray, (nCols,nRows), None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (13,17), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        img = cv.drawChessboardCorners(img, (nCols,nRows), corners2, ret)
        cv.imshow('Imagens Capturadas e Pontos Detectados', img)
        cv.imwrite('imagem_compontos.jpg', img)
        cv.waitKey(500)

#Calibracao
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
np.savez('./data/calibL.npz', mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)
print("Camera matrix : \n")
print(mtx)
print("dist : \n")
print(dist)
print("rvecs : \n")
print(rvecs)
print("tvecs : \n")
print(tvecs)


img = cv.imread('imageR14.jpg')
h, w = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))


# undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]

cv.imwrite('imagem_ajustada.jpg', dst)

# # Re-projection Error
# mean_error = 0
# for i in xrange(len(objpoints)):
#     imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
#     error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2)/len(imgpoints2)
#     mean_error += error
# print( "Erro total:{}".format(mean_error/len(objpoints)) )
# # Erro total:0.0337697157082

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
dst = cv.cvtColor(dst, cv.COLOR_BGR2RGB)

plt.subplot(1,2,1), plt.imshow(img, 'brg')
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2), plt.imshow(dst, 'brg')
plt.title('Imagem Corrigida'), plt.xticks([]), plt.yticks([])
plt.show()

cv.destroyAllWindows() # fecha as janelas abertas