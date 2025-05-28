###############################################################################
#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
# el dí­a correspondiente. 
#  Si introducimos otro número nos da un error.
# ################################################################################

dia = int(input ("Escribe un dia del 1 al 7: "))

match dia:
    case 1:
        print("lunes")
    case 2:
        print ("martes")
    case 3:
        print ("miercoles")
    case 4:
        print ("jueves")
    case 5: 
        print ("viernes")
    case 6:
        print ("sabado")
    case 7:
        print ("domingo")
    case _:
        print ("El dia elegido no existe")
