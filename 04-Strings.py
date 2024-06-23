### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

#llamar a una variable y mostrarlo con salto de linea 
my_primer_apellido_es = "este es mi primer apellido\nHumire"
print(my_primer_apellido_es)

# con tabulacion 
my_primer_Nombre_es = "\teste es mi Nombre : Marcos"
print(my_primer_Nombre_es)
# con tabulacion y salto de linea 
my_primer_Nombre_es = "\teste es mi Nombre : \n Marcos"
print(my_primer_Nombre_es)

#Formateo 
nombre, apellido , edad = "Elias" , "Humire", 20
print("Mi nombre es {} {} y mi edad es {}" .format(nombre, apellido,edad))
print("Mi nombre es %s %s y mi edad es %s" %(nombre,apellido,edad))
print("Mi nombre es " + " " + nombre+" "+ apellido+"  "+"y Mi edad es " + str(edad))
# Una manera mas rapida 
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")

# Desempaquetado de caracteres 
lenguage = "python"
a, b, c, d, e, f, = lenguage
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division 
lenguage_slize = lenguage[1:4]
print(lenguage_slize)

lenguage_slize = lenguage[1]
print(lenguage_slize)

# Para dar la vuelta 

reversed_lenguaje = lenguage[::-1]
print(reversed_lenguaje)


#Funciones 

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count("t"))
print(lenguage.isnumeric())
print("10".isnumeric())
print(lenguage.lower())
print(lenguage.lower().isupper())
print(lenguage.startswith("Py"))
print("Py" == "py")