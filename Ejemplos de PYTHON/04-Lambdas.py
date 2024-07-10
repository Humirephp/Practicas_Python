### Lambdas ###

sumar_ = lambda num1, num2 : num1 + num2
print(sumar_(2, 6))
multiplicar_ = lambda num1, num2 : num1 * num2 - 3
print(multiplicar_(2, 6))
dividir_ = lambda num1, num2 : num1 / num2
print(dividir_(10, 5))

def sum_three_values(value):
    return lambda num1, num2: num1 + num2 + value

print(sum_three_values(5)(2, 6))