#robot.py

import math 
#import sympy
import numpy as np


def transf_homogenea(theta, d, a, alpha):	
	#
	# Retorna a matriz transformacao homogenea entre juntas sucessivas
	# Os parametros de entrada estao de acordo com a convecao de Denavit Hartenberg
	#
	theta = math.radians(theta)
	alpha = math.radians(alpha)
	A = np.array([[math.cos(theta),  -math.cos(alpha)*math.sin(theta),   math.sin(alpha)*math.sin(theta),   a*math.cos(theta)],
       	 		 [math.sin(theta) ,   math.cos(alpha)*math.cos(theta),  -math.sin(alpha)*math.cos(theta),   a*math.sin(theta)],
    			 [ 0         ,         math.sin(alpha)     ,       math.cos(alpha)       ,        d      ],
    			 [ 0         ,             0          ,          0             ,        1      ]])
	return A
	#Fim da funcao DH

# Parâmetros de DH
# Definir Theta equivale a Cinematica direta 
Theta = [0., 0., 0., 0., 0.] #Variavel de junta Theta 
theta = [Theta[0]+0., Theta[1]+90., Theta[2]+0. , Theta[3]-90., Theta[4]+0.] 
d =  [97., 0., 0., 22., 156.] #Fixo
a = [13., 103., 99., -31., 0.] #Fixo
alpha =[90., 0., 0., -90., 0.] #Fixo

# Transformações homogêneas dos elos
A1 = transf_homogenea(theta[0], d[0], a[0], alpha[0])
A2 = transf_homogenea(theta[1], d[1], a[1], alpha[1])
A3 = transf_homogenea(theta[2], d[2], a[2], alpha[2])
A4 = transf_homogenea(theta[3], d[3], a[3], alpha[3])
A5 = transf_homogenea(theta[4], d[4], a[4], alpha[4])

print(A5)

# Transformação do ultimo sistema de coordenadas para a base

T02 = np.matmul(A1, A2)
T03 = np.matmul(T02, A3)
T04 = np.matmul(T03, A4)
T05 = np.matmul(T04, A5)

print("Cinematica Direta: ")
print(T05)+