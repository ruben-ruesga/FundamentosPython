################################################################################
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
################################################################################

# hipotenusa ** 2 = cateto1 ** 2 + cateto2 ** 2

## el operador doble ** permite elevar un numero a una potencia n 
##para operaciones matematicas avanzadas importamos la libreria math

import math

cateto1 = int(input("ingresa valor de Cateto 1:  "))
cateto2 = int(input("ingresa valor de Cateto 2:  "))

hipotenusa =  math.sqrt(cateto1 ** 2 + cateto2 ** 2)

print("La hipotenusa del triangulo es: " + str(hipotenusa))