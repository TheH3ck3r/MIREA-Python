deriv = lambda f: lambda x: (f(x + 10**-6) - f(x - 10**-6)) / (2 * (10**-6))
result = deriv(lambda x: x ** 3)(5)
print(result)