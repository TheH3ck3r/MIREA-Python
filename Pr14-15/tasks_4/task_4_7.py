Z = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))
fact = Z(lambda f: lambda n: 1 if n == 0 else n * f(n - 1))

print(fact(5))