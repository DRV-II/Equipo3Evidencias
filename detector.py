"""
Equipo 3:

David Román Velasco - A01639645
Edgar Cruz Vazquez - A01730577
Sergio Pedroza - A01636537
Diego Velázquez - A01632240

Fuentes de referencias:

Errodringer. (13 octubre 2020). 😃 Reconocimiento Facial 🧒 PYTHON - OPENCV (3 minutos en Español) *2021* [Video]. Recuperado de: https://www.youtube.com/watch?v=i7J40MnQUSg

"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

# David
def conv_helper(fragment, kernel):
    """ multiplica 2 matices y devuelve su suma"""
    
    f_row, f_col = fragment.shape
    k_row, k_col = kernel.shape 
    result = 0.0
    for row in range(f_row):
        for col in range(f_col):
            result += fragment[row,col] *  kernel[row,col]
    return result

def main(name):
    path = r'D:\Work\SemanaTec\2do semestre\1er periodo\Tareas\semena-tec-tools-vision-master\semena-tec-tools-vision-master\Scripts\Proyecto Vision\Turquia.jpg'
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    cv2.imshow(name, gray) 
    #kernel = np.ones((3,3)) #Se usa el filtro estandar
    kernel = np.array([[1,1,1], [0,0,0], [-1, -1, -1]]) #Se usa el filtro Prewitt
    resultado = convolution(gray, kernel)

def escala_grises(name):
    path = r'D:\Work\SemanaTec\2do semestre\1er periodo\Tareas\semena-tec-tools-vision-master\semena-tec-tools-vision-master\Scripts\Proyecto Vision\Turquia.jpg'
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    cv2.imshow(name, gray) 
