### Condicionales ###

my_condicion = False

if my_condicion: # Es lo mismo que if my_condicion == True:
    print("Se ejecuta la condicion de if")

my_condicion = 5 * 2

if my_condicion == 10:
    print("La respuesta es correcta")
else:
    print("no es correcta")

# Este es otro ejemplo
Nombre = "Elias"
Nombre = input ("¿Cual es tu nombre?")
if Nombre == "Elias":
    print("SU nombre es correcto")
else :
    print("el nombre no es correcto")


#Otro ejemplo con num
Num1 = input("Ingrese un numero")
Num2 = input("Ingrese el segundo numero")
# Convierte las entradas a enteros
Num1 = int(Num1)
Num2 = int(Num2)
# Calcula la respuesta multiplicando Num1 y Num2
respuesta = Num1 * Num2
# Imprime la respuesta de la multiplicación
print("la respuesta de la mulitiplicacion es",respuesta)
# Compara la respuesta con 10
if respuesta == 10:
    print("La respuesta es correcta")
elif respuesta>10:
    print("El número es mayor que 10")
else:
    print("El numero es menor")









