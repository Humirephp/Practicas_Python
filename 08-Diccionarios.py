### Diccionarios ###

my_dict = dict()
my_other_dict = {}
print(type(my_dict))

print(type(my_dict))
print(type(my_other_dict))
#Estructura para relacionar Datos 
my_other_dict = {"Nombre":"Elias", "Apellido":"Humire", "Edad" :20 , 1:"PHP"}
my_dict = {
     "Nombre":"Elias",
     "Apellido":"Humire",
     "Edad" :20 ,
     "Lenguajes": {"Pyhon", "Html", "PHP"},
     1:1.70
}
print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"]) 
my_dict["Nombre"] = "Jesus"
print(my_dict["Nombre"])

print(my_dict[1])
# De esta manera agregamos un nuevo campo al diccionario
my_dict["Ciudad"] = "Tacna"
print(my_dict)
#Para eliminar un solo elemnto en nuestro diccionario
del my_dict["Ciudad"]
print(my_dict)

print("Apellido"in my_dict)
print("Ciudad"in my_dict)
print(my_dict["Apellido"])
print(my_dict["Nombre"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
my_new_dict = my_other_dict.fromkeys(("Nombre" , 1, "Calle", "Edad"))
my_new_dict["Calle"] = "Tacna"
my_new_dict["Nombre"] = "Mathias"
my_new_dict["Edad"] = 20
my_new_dict[1] = "PHP"
print(my_new_dict)

my_list = ["Nombre", 1 , "Calle"]

my_new_dict = dict.fromkeys((my_list))
print(my_other_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Calle", "Edad"))
print(my_new_dict)
my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_other_dict))
print(set(my_other_dict))