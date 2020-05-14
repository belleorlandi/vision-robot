# funtions_robot.py
#import math 
#import sympy
import numpy as np

def deg2rad(deg):
	#
	#Transforma angulos em graus para radianos
	#
	rad = deg * math.pi / 180
	return 	rad
	#Fim da funcao graus para radianos

def transf_homogenea((theta, d, a, alpha)):	
	#
	# Retorna a matriz transformacao homogenea entre juntas sucessivas
	# Os parametros de entrada estao de acordo com a convecao de Denavit Hartenberg
	#
	A = np.array([[math.cos(theta),  -math.cos(alpha)*math.sin(theta),   math.sin(alpha)*math.sin(theta),   a*math.cos(theta)],
       	 		 [math.sin(theta) ,   math.cos(alpha)*math.cos(theta),  -math.sin(alpha)*math.cos(theta),   a*math.sin(theta)],
    			 [ 0         ,         math.sin(alpha)     ,       math.cos(alpha)       ,        d      ],
    			 [ 0         ,             0          ,          0             ,        1      ]])
	return A
	#Fim da funcao DH


class Robot:
	"""docstring for ClassName"""
	def __init__(self, name):
	#Define variaveis do manipulador
		self.name = name
		self.DOF = 5
		# Tabela DH
		self.theta = np.array([0, 0, 0, 0, 0])
		self.d = np.array([0, 0, 0, 0, 0.050])
		self.a = np.array([-0.0265, 0.1029, 0.0957, 0.0300, 0])
		self.alpha = np.array([math.pi/2, 0, 0, -math.pi/2, 0])
		self.tool = np.array([0,    0.1, 0, 0])
		self.base = np.array([0, 0.0593, 0, 0])

	def hello(self):
		print 'Ola, meu nome e', self.name , '\n'

	def elo(self, n):
		theta = self.theta[n]
		d = self.d[n]
		a = self.a[n]
		alpha = self.alpha[n]
		return theta, d, a, alpha


__version__ = '0.1'
