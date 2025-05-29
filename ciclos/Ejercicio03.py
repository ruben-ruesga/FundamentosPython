################################################################################
# Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
#  y la media de todos los números introducidos.
################################################################################

suma = 0
numeros = 0

while True:
    numero = int(input("ingresa un numero: "))
    if numero == 0: 
        print("la suma de los numeros ingresados es: ", suma)
        print("La media de los numeros es:", suma / numeros)
        break
    #suma = suma + numero
    suma += numero
    #numeros = numeros + 1
    numeros += 1