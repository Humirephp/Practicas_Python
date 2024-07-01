### Exception ###

print(5 + int("4"))

numberUno = 10
numberDos = 12
numberDos = "12"


# try except
try:
   print(numberUno + numberDos)
   print("No se ha producido un error")
except:
    # Esto se ejecuta si no se produce una exception
    print("Se ha producido un error")

# try except else y finally

try:
   print(numberUno + numberDos)
   print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Esto se ejecuta si no se produce una exception
    print("La ejecucion continua correctamente")
finally: # Opcional
    # Se ejecutara siempre 
    print("La ejecucion continua")

# La captura de exceptions por tipo

try: 
   print(numberUno + numberDos)
   print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")


#Captura de la informacion de la Exception

try: 
   print(numberUno + numberDos)
   print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as puedesEscribirCualquierCosa:
    print(puedesEscribirCualquierCosa)
