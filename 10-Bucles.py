### Bucles ###

# While 

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition +=2
else: #Es opcional
    print("Los numeros son menores que 10")

print("La ejecucion continua")
 
while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
      print("Se detiene la ejecucion")
      break
    print(my_condition)

print("La ejecucion continua")


#For
print("----Primera lista----")
my_list = [20, 40, 24, 45, 65, 54, 45]
for element in my_list:
    print(element)

print("----Segunda lista----")
my_tuple = (25, 1.80, "Elias" , "Humire", "Tacna")
for element in my_tuple:
    print(element)

print("----Tercera lista----")
my_set = {"Mateo", "Peru", 34}
for element in my_set:
    print(element)

print("----Cuarta lista----")
my_dict = {"Nombre": "Elias", "Apellido": "Humire", "Edad": 24, 1:"Tacna" }
# --- de esta manera tambien funciona ---
# for element in my_dict.values():
# print(element)
# ----Muestra los elementos con sus datos ----
# for element in list(my_dict.values()):
 # print(element)
 #----------------#
print("---la ejecucion continua---")

for element in my_dict:
     print(element)
     if element == "Edad":
         continue
     print("Se ejecuta")
else:
      print("----El bucle for para diccionario a finalizado----")
