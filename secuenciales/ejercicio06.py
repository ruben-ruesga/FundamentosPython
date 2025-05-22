#################################################################################
#Calcular la media de tres números pedidos por teclado
#################################################################################
#Análisis
#Tenemos que leer tres números y calcular la media. Suma de los tres partido 3.
#Datos de entrada: los tres números (real)
#Información de salida: la media (real)
#Variables: num1,num2,num3, media (Real).
#################################################################################
#Diseño
#1. Leer los tres nÃºmeros
#2. Calcular la media: (num1+num2+num3)/3
#3. Mostrar la media
#################################################################################

print("programa que promedia 3 numeros")
print("")

numero1 = int(input("ingresa el primer numero: "))
numero2 = int(input("ingresa el segundo numero: "))
numero3 = int(input("ingresa el tercer numero: "))

promedio = (numero1 + numero2 + numero3) / 3

print("el promedio de los numeros es:", promedio)