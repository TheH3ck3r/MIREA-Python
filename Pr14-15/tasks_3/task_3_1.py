I = lambda x: x
K = lambda x: lambda y: x
KI = lambda x: lambda y: y

С = lambda f: lambda a: lambda b: f(b)(a)

M = lambda x: x(x)

power = lambda x: lambda y: x ** y

print(I(42))
print(K(1)(2))
print(KI(1)(2))
print(C(C(power))(2)(5))
print(M(lambda x: 42))