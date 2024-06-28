### Sets ###
# Recordar que no podemos acceder a un indice ya que no esta ordenado 
my_set = set()
my_other_set ={}

print(type(my_set))
print(type(my_other_set)) # Es un diccionario

my_other_set = {"Elias", "Humire", 20}
print(type(my_other_set))

print(len(my_other_set))
#un set add no muestra elementos ordenados 
my_other_set.add("Mathias") #Recordar que set no es una extructura ordenada
print(my_other_set)

my_other_set.add("Mathias")# Im set no admite repeticiones 
print(my_other_set)

#Muestra si el dato existe (verdadero) y si no existe (falso)
print("Mathias"in my_other_set)
print("Marcios"in my_other_set)

#Para eliminar dato 
my_other_set.remove("Mathias")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))
#Eliinar elementos por completo de una lisra 
del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Fernando", "Pablo", 25}
my_list = list(my_set)
print(my_list)
print(my_list[0])
#Para unir varias propiedades 
my_other_set = {"Java", "Python", "PHP"}
my_new_set = my_set.union(my_other_set)
print(my_new_set)
#Se puede agregar elementos de esta manera ignorando los dos primero unions 
print(my_new_set.union(my_new_set).union(my_set).union({"HTML", "C#"}))
#Muestra las  diferencias 
print(my_new_set.difference(my_set))