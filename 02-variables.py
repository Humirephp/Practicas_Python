# Definir Variables  String
Nombre = "Mateo"
print (Nombre)
# Una forma correcta es tambien 
mi_nombre_es = "MARCOS"
print (mi_nombre_es)
# Definir variable int
definir_int = 5
print(definir_int)
# Convertir un numero entero a una cadena de caravteres string
definir_str = str(definir_int)
print(definir_str)
print(type(definir_str))

# Definir variable bool 
definir_bool = False
print (definir_bool)

# Concatenacion de variables en print  
print(mi_nombre_es, definir_int, definir_bool)
print("Este es el valor de:", definir_bool)

# Akgunas Funciones del sistema para mostrar el numero de caracteres  
print (len(mi_nombre_es)) 

# Definir Variables en una sola linea 
edad, dni, apellido, apodo  ="18" , "9999" , "Acero", "Leon"
print("- mi edad es :", edad, " - mi numero de DNI es :", dni ,"- Mi apellido es :", apellido, " - mi apodo es :" ,apodo)

#Inputs 
name = input ("¿Cual es tu nombre?")
age = input ("¿Cual es tu edad?")

print("tu nombre es :", name)
print("tu edad es :", age) 

# Forzamos el tipo
address: str = "Esto es elemental"
print(type(address))