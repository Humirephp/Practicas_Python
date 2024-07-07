### List- Comprehension ### 

my_range = range(8)
print(list(my_range))

autos = ["Lamborgini", "Nisan"]
Listas = [i for i in autos]
print(Listas)

my_list = [20 , 30 , 24 , 19, 20]
print(my_list)

List = [i + 1 for i in range(8)]
print(List)

List = [i * 1 for i in range(8)]
print(List)

List = [i * i for i in range(8)]
print(List)

def sumas(num):
    return num + 5

List = [sumas(i) for i in range(8)]
print(List)

