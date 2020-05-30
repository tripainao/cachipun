#programa para jugar cachipún!

import sys
import random
import os

#limpiar consola
os.system("clear")

#echar una mirada a los argumentos
print("nombre del script: ", sys.argv[0])
print("Numero de arguments: ", len(sys.argv))
print("argumentos: " , str(sys.argv))

numArgs = len(sys.argv)

#validar que sea un solo argumento, ni mas ni menos
if ( numArgs < 2 ):
    print("Debe tener un sólo argumento!, ej: python main.py [arg]")
    quit()
elif ( numArgs > 2 ):
    print("Debe ingresar un solo argumento!, ej: python main.py [arg]")
    sys.exit()
else:
    print("Bienvenido a cachipun!")

# dejamos el argumento de la jugada en una variable
mijugada = sys.argv[1]
if (mijugada in ["piedra", "papel", "tijera"]):
    print("Ha seleccionado la jugada: ", mijugada)
else:
    print("Debe ingresar: piedra, papel o tijera")
    quit();

jugadarobot = (random.randint(1,3))

print("la jugada de la maquina es: ")
if (jugadarobot == 1):
    print("piedra")
if (jugadarobot == 2):
    print("papel")
if (jugadarobot == 3):
    print("tijera")        
#1: piedra
#2: papel
#3: tijera

#Computador juega tijera Ganaste
# python juego.py tijera
#Computador juega tijera Empataste
# python juego.py tijera
#Computador juega piedra Perdiste

#1: piedra
if (jugadarobot == 1):
    if (mijugada == "piedra"):
        print ("empate")
    elif (mijugada == "papel"):
        print ("perdiste")
    elif (mijugada == "tijera"):
        print ("ganaste")    
#2: papel
elif (jugadarobot == 2):
    if (mijugada == "piedra"):
        print ("perdiste")
    elif (mijugada == "papel"):
        print ("empate")
    elif (mijugada == "tijera"):
        print ("ganaste")   
#3: tijera
elif (jugadarobot == 3):
    if (mijugada == "piedra"):
        print ("ganaste")
    elif (mijugada == "papel"):
        print ("perdiste")
    elif (mijugada == "tijera"):
        print ("empate")         

