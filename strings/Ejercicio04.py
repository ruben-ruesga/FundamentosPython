################################################################################
# Suponiendo que hemos introducido una cadena por teclado que representa una frase 
# (palabras separadas por espacios), realiza un programa que cuente cuantas 
# palabras tiene.
# ################################################################################

phrase = input("Escribe una frase: ")

words = phrase.split(" ")

print(f"La frase contiene { len(words) } palabras")