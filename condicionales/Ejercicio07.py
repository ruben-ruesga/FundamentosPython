################################################################################
#  Realiza un algoritmo que calcule la potencia, para ello pide por teclado 
# la base y el exponente. Pueden ocurrir tres cosas:
#  * El exponente sea positivo, sólo tienes que imprimir la potencia.
#  * El exponente sea 0, el resultado es 1.
#  * El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
################################################################################

base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

if exponente > 0:
    print(f"El numero { base } elevado a la { exponente } es { base ** exponente }")
elif exponente == 0:
    print(f"El numero { base } elevado a la 0 es 1")
else:
    print(f"El numero { base } elevado aq la { exponente } es 1/ { base }^{ abs(exponente )}")