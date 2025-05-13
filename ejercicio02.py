################################################################################
#Calcular el perí­metro y área de un rectángulo dada su base y su altura.
################################################################################

print("programa que calcula area y perimetro de un rectangulo")

altura = input("Ingresa la Altura: ")
altura = int(altura)
base = int(input("Ingresa la base: "))

perimetro = base + altura + base + altura
area = base * altura

print("El area del rectangulo es: " + str(area))
print("el perimetro del rectangulo es: " + str(perimetro)) 