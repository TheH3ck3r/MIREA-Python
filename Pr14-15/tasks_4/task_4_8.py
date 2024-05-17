Z = lambda g: (lambda x: g(lambda v: x(x)(v))) \
            (lambda x: g(lambda v: x(x)(v)))

fact = Z(lambda f: lambda n: 1 if n == 0 else n * f(n - 1))

result = fact(5)

print(result)