true = lambda x: lambda y: x
false = lambda x: lambda y: y

stringify = lambda b: "Да" if b(true)(false) == true else "Нет"
inv = lambda x: x(false)(true)

eq = lambda p: lambda q: p(q)(inv(q))
print(stringify(eq(true)(true)))  # Да
print(stringify(eq(false)(true))) # Нет
print(stringify(eq(true)(false))) # Нет
print(stringify(eq(false)(false))) # Да