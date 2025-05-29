################################################################################
#  Crea una aplicación que permita adivinar un número. La aplicación genera un 
#  número aleatorio del 1 al 100. A continuación va pidiendo números y va 
#  respondiendo si el número a adivinar es mayor o menor que el introducido,
#  a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
#  El programa termina cuando se acierta el número (además te dice en cuantos 
# intentos lo has acertado), si se llega al limite de intentos te muestra el 
# número que había generado.
################################################################################

import random

aleatorio = random.randint(1,100)
intentos = 10

while True:
    numero = int(input("Adivina el numero: "))
    if aleatorio == numero:
        print("Adivinaste el numero!")
        print(f"Lo hiciste en { intentos } intentos")
        break
    elif numero > aleatorio:
        print("ingresa otro mas pequeño: ")
        intentos = intentos - 1
    else:
        print("ingresa otro mas grande: ")
        intentos = intentos - 1

    if intentos == 0: print("Perdiste!!")