"""
Equipo 3:

David Román Velasco - A01639645
Edgar Cruz Vazquez - A01730577
Sergio Pedroza - A01636537
Diego Velázquez - A01632240

Fuentes de referencias:

Errodringer. (13 octubre 2020). 😃 Reconocimiento Facial 🧒 PYTHON - OPENCV (3 minutos en Español) 2021 [Video]. Recuperado de: https://www.youtube.com/watch?v=i7J40MnQUSg

"""

import numpy as np
import cv2
import matplotlib.pyplot as plt


# Sergio
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