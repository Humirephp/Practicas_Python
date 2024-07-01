### Modules ###

import my_module

my_module.suma(10, 14, 20)
my_module.printValue("Hola Mundo")

from my_module import printValue, suma

suma(10, 14, 20)
printValue("Hola Mundo")

import math

print(math.pi)
print(math.pow(2, 3))

from math import pi as PY_VALUE
print(PY_VALUE)