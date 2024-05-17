true = lambda x: lambda y: x
false = lambda x: lambda y: y

stringify = lambda p: p("Да")("Нет")

K = lambda x: lambda y: x

def either(x):
    return lambda y: K(x)(y)

# Примеры использования
print(stringify(either(true)(false)))  # Да
print(stringify(either(false)(false)))  # Нет