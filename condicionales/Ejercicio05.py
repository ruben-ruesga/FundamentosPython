################################################################################
# Escribe un programa que pida un nombre de usuario y una contraseña 
# y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
# sino se da un error.
################################################################################

db_username = "pepe"
db_password = "asdasd"

username = input("Ingresa tu usuario: ")
password = input("Ingresa tu contraseña: ")

if db_username == username and db_password == password:
    print("Bienvenido al sistema")
else:
    print("Usuario y contraseña incorrectos")