# main.py
#import sys
#import cv2 #OpenCV
#import sympy #Symbolic computation
from functions_robot import *


# -------------------------------------------
# Programacao Visao Computacional
#--------------------------------------------


# Retorna (x,y,z) - coordenadas destino do elemento final do manipulador.


# -------------------------------------------
# Programacao Cinematica 
#--------------------------------------------
print '==========================================='
print '       PROJETO - ROBO MANIPULADOR'
print '===========================================', "\n" 

r = Robot('robot') 
r.hello()

print '-------------------------------------------'
print '           Cinematica Direta'
print '-------------------------------------------', "\n" 

 
r.theta = np.array([0, 0, 0, 0, 0]) #Angulos das juntas desejado para a posicao destino

print '>>>>> TRANSFORMACAO HOMOGENEA DE CADA ELO', "\n" 

print 'Parametros elo 1', "\n" 
print r.elo(0) , "\n" 
print 'Transformacao homogenea elo 1:' , "\n" 
T1 = transf_homogenea(r.elo(0))
print  T1, "\n" 

print 'Parametros elo 2', "\n" 
print r.elo(1) , "\n" 
print 'Transformacao homogenea elo 2:' , "\n" 
T2 = transf_homogenea(r.elo(1)) 
print T2, "\n" 

print 'Parametros elo 3', "\n" 
print r.elo(2) , "\n" 
print 'Transformacao homogenea elo 3:' , "\n" 
T3 = transf_homogenea(r.elo(2))
print  T3, "\n" 

print 'Parametros elo 4', "\n" 
print r.elo(3) , "\n" 
print 'Transformacao homogenea elo 4:' , "\n" 
T4 = transf_homogenea(r.elo(3))
print  T4, "\n" 

print 'Parametros elo 5', "\n" 
print r.elo(4) , "\n" 
print 'Transformacao homogenea elo 5:' , "\n" 
T5 = transf_homogenea(r.elo(4))
print  T5, "\n" 

print '>>>>> TRANSFORMACAO HOMOGENEA DE 1 A 5', "\n" 

Tf = T1 * T2
print Tf