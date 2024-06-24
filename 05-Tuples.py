### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (24, 1.70, "Kevin", "Kevin", "Humire")
my_other_tuple = (20, 26, 69)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4])  Index Error----
#print(my_tuple[-6]) Index Error----

print(my_tuple.count("Kevin"))
print(my_tuple.index("Humire"))
print(my_tuple.index("Kevin"))

#my_tuple[5] = 1.70 esto es un error ...

#Para concatenar tuples 
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])
