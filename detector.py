"""
By Abhisek Jana
code taken from https://github.com/adeveloperdiary/blog/tree/master/Computer_Vision/Sobel_Edge_Detection
blog http://www.adeveloperdiary.com/data-science/computer-vision/how-to-implement-sobel-edge-detection-using-python-from-scratch/

Modificado por Benjamin Valdes


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

# Edgar
def convolution(image, kernel):
    """Aplica una convolucion sin padding (valida) de una dimesion 
    y devuelve la matriz resultante de la operación
    """

    image_row, image_col = image.shape #asigna alto y ancho de la imagen 
    kernel_row, kernel_col = kernel.shape #asigna alto y ancho del filtro
   
    output = np.zeros(image.shape) #matriz donde guardo el resultado
   
    for row in range(image_row):
        for col in range(image_col):
                output[row, col] = conv_helper(
                                    image[row:row + kernel_row, 
                                    col:col + kernel_col],kernel)
             
    plt.imshow(output, cmap='gray')
    plt.title("Output Image using {}X{} Kernel".format(kernel_row, kernel_col))
    plt.show()
 
    return output

# David
def main(name):
    """Es la función que le corresponde a la primera opción del menu, la cual convierte
    una imagen a escala de grises y llama a la función convolution(image, kernel)
    """
    
    path = r'D:\Work\SemanaTec\2do semestre\1er periodo\Tareas\semena-tec-tools-vision-master\semena-tec-tools-vision-master\Scripts\Proyecto Vision\Turquia.jpg'
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    cv2.imshow(name, gray) 
    #kernel = np.ones((3,3)) #Se usa el filtro estandar
    kernel = np.array([[1,1,1], [0,0,0], [-1, -1, -1]]) #Se usa el filtro Prewitt
    resultado = convolution(gray, kernel)

def escala_grises(name):
    """Es uyna función que convierte una imagen a escala de grises"""
    
    path = r'D:\Work\SemanaTec\2do semestre\1er periodo\Tareas\semena-tec-tools-vision-master\semena-tec-tools-vision-master\Scripts\Proyecto Vision\Turquia.jpg'
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray.shape)
    cv2.imshow(name, gray) 

# Diego
def detectar_cara():
    """
    Funcion detectar_cara
    En la funcion mediante el cascade clasifier busca encontrar una cara al momento de activar la camara
    de la computadora o ordenador, en cuenta la encuentra la enmarca dentro de un cuadro azul de 4px y despliega el texto
    "Face Detected"
    Input:La funcion no recibe nada.
    Output:La funcion despliega la camara intentando hacer la deteccion de cara
    """
    
    haar_file = 'haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(haar_file)
    webcam = cv2.VideoCapture(0)

    while True:
        (_, im) = webcam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x,y), (x+w, y+h), (255, 0, 0), 4)
        cv2.putText(im,'Face detected',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
        cv2.imshow('OpenCV', im)
        
        key = cv2.waitKey(10)
        if key == 27:
            break
# Sergio
"""
Se despliega el menu principal del programa en el cual el usuario puede elegir las acciones que quiera realizar
"""

menu = 0
while menu != 3:
    print("""--------MENU--------
    1. Cambiar imagenes a escala de grises
    2. Usar reconocimiento facial
    3. Salir\n""")
    menu = int(input("Seleccione opción del menu: "))
    if menu == 1:
        name = input("Ingrese nombre de la imagen: ")
        #path = input("Ingrese directorio de la imagen: ")
        #path = "D:\\Work\\SemanaTec\\2do semestre\\1er periodo\\Tareas\\semena-tec-tools-vision-master\\semena-tec-tools-vision-master\\Scripts\\Proyecto Vision\\Turquia.jpg"
        #print("Converted to Gray Channel. Size : ")
        #escala_grises(name)
        main(name)
    elif menu == 2:
        detectar_cara()
    elif menu == 3:
        print("Adios :D")
    else:
        print("Elije opción valida")
        continue