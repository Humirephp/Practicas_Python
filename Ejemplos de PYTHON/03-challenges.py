### challenges ###

"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0 :
          print("fizzbuzz")
        elif num % 3 == 0:
           print("fizz")
        elif num % 5 == 0:
           print("buzz")
        else:
          print(num)
fizzbuzz()

"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""

def is_anagram(text1, text2):
   if text1.lower() == text2.lower():
      return False
   return sorted(text1.lower()) == sorted(text2.lower())

print(is_anagram("Amor", "Roma"))
print(is_anagram("vela", "lave"))
print(is_anagram("Amor", "Chile"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""
def FIBONACCI():
   
   num1 = 0
   num2 = 1

   for numero in range(0, 51):
      print(num1)
      fib = num1 + num2
      num1 = num2
      num2 = fib
FIBONACCI()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
def is_prime():
   
    for num in range(1, 101):


        if num >= 2:
     
           is_divisible = False
   
           for index in range(2, num):
               if num %  index == 0:
                   is_divisible = True
                   break
       
           if not is_divisible:
                print(num)

is_prime()

"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
   text_len = len(text)
   reverse_text = ""
   for index in range(0, text_len):
      reverse_text += text[text_len - index - 1]
   return reverse_text

print(reverse("Hola Mundo"))