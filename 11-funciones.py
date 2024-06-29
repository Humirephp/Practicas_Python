### Functions ###

def my_function():
    print("Esto es una funcion")
    
my_function ()


def sum_dos_values (num1, num2, num3):
    print(num1 + num2 + num3)

sum_dos_values(5, 7, 7)
sum_dos_values(6, 70, 8)


def sum_tres_values (num1, num2, num3):
    my_sum = num1 + num2 + num3
    return my_sum


my_result = sum_tres_values(20, 10, 30)
print(my_result)

my_result = sum_dos_values(5, 7, 7)
print(my_result)

def print_name(nombre, apellido):
    print(f"{nombre} {apellido}")

print_name(nombre= "Elias", apellido= "Humire")


def mostras_datos_person (nombre, apellido, ciudad):
    print(f"{nombre} {apellido} {ciudad}")

mostras_datos_person("Elias", "Humire", "Tacna")


def mostrar_datos_persona(*texts):
    for text in texts:
        print(text.upper())



mostrar_datos_persona("Hola", "php", "html")
mostrar_datos_persona("Hola")
