true = lambda x: lambda y: x
false = lambda x: lambda y: y

inv = lambda p: lambda x: lambda y: p(y)(x)
stringify = lambda p: p("Да")("Нет")

print(stringify(inv(true))) # Нет
print(stringify(inv(inv(inv(false))))) # Да
