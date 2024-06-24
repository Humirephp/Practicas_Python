## Listas ##

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [20 , 30 , 24 , 19,20]
print(my_list)
print(len(my_list))

my_other_list = [24, 1.80, "Humire" , "Elias"]
print(my_other_list)
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(20))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError
 
año, altura , apellido, nombre, = my_other_list
print(nombre)

print(my_list + my_other_list)

my_other_list.append("Ingenieria de Software")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list[1] = "negro"
print(my_other_list)

my_other_list.remove("negro")
print(my_other_list)

my_list.remove(20)
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)
#Eliminar elementos de una lista 
del my_list[1]
print(my_list)

#Para copiar unalista antes de eliminarla
my_new_list= my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:1])

lista_de_alumnos = ["Juan", "Lucas", "Mateo", "Jesus"]
print(lista_de_alumnos)

print(lista_de_alumnos.pop(2))
print(lista_de_alumnos)
#Eliminar elementos de una lista 
del lista_de_alumnos[1]
print(lista_de_alumnos)
