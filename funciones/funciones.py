print("soy una funcion")
print()
number = int("15")
longitud = len("hello")
my_str = str(26)

## Funciones de Python
'''
def name (args):
    return
'''

def saludo():
    print("Helloooooo!")

def cuenta_diez():
    for i in range(10):
        print(i,end=' - ')
    print()

saludo()
saludo()
cuenta_diez()
cuenta_diez()

def saluda_a(name):
    print ("hello", name)

saluda_a("Peter")    
saluda_a("Tony")
saluda_a("Bruce")

def reverse(name):
    print(name[::-1])

reverse("Francisco")
reverse("Universidad")
reverse("EVND")

def suma(num1,num2):
    resultado = num1 + num2
    return resultado

resultado = suma(23,26)
print(resultado)

def resta(num1, num2):
    return num1 - num2

resultado = resta(23,26)
print(resultado)