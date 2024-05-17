true = lambda x: lambda y: x
false = lambda x: lambda y: y

stringify = lambda p: p("Да")("Нет")

print(stringify(true))
print(stringify(false))