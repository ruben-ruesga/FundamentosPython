################################################################################
#Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
################################################################################

numero1 = int(input("inserta un numero: "))
numero2 = int(input("inserta otro numero: "))

suma = numero1 + numero2
resta = numero1 - numero2

print("la suma es: ", suma)
print("la resta es: ", resta)
print("la multiplicacion es:", numero1 * numero2)
print("la division es:", numero1 / numero2)
print("la division entera es:", numero1 // numero2)
print("el residuo es:", numero1 % numero2)

import math
print("el 1.7 redondeado es:",round(1.7))