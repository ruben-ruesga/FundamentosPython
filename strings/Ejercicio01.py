################################################################################
# Escribir por pantalla cada carácter de una cadena introducida por teclado
#################################################################################

my_string = input("Ingresa un texto: ")

print(my_string)

for letra in my_string:
    print(letra, end=" - ")

print()

# la funcion len nos da el tamaño de un string
for index in range(len(my_string)):
    print(f"[{index}] = {my_string [index] }")

other_string ="Prueba"

print(other_string[0])
print(other_string[3])
print(other_string[5])
