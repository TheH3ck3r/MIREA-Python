K = lambda x: lambda y: x
KI = lambda x: lambda y: y

Vireo = lambda x: lambda y: lambda f: f(x)(y)

pair = Vireo
my_tuple = pair(3)(4)
print(my_tuple(K))
print(my_tuple(KI))