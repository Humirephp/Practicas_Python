#### Clases ####

class Persona:
    pass 

print(Persona)
print(Persona())

#Esto es una manera 
class Person:
    #Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

my_person = Person("Elias", "Humire")
print(f"{my_person.nombre} {my_person.apellido}")
#Esto es otra manera 
class Estudiante:
    #Constructor
    def __init__(self, nombre, apellido, ciudad  = "Tacna"):
        self.nombre_completo = f"{nombre} {apellido} ({ciudad})"

    def walk (self):
        print(f"{self.nombre_completo} Esta caminando" )


my_person = Estudiante("Mateo", "Humire")
print(my_person.nombre_completo)
my_person.walk()

my_otra_persona = Estudiante("Mateo", "Humire", "Tacna")
print(my_otra_persona.nombre_completo)
my_otra_persona.walk()

my_otra_persona.nombre_completo = "Elias Humire (el legendario jugador de mobile legends)"
print(my_otra_persona.nombre_completo)

my_otra_persona.nombre_completo = 500
print(my_otra_persona.nombre_completo)