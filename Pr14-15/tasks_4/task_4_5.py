true = lambda x: lambda y: x
false = lambda x: lambda y: y


both = lambda p: lambda q: p(q)(p)


def stringify(boolean_function):
    return "Да" if boolean_function == true else "Нет"


print(stringify(both(true)(true)))   # Да
print(stringify(both(false)(true)))  # Нет
print(stringify(both(true)(false)))  # Нет
print(stringify(both(false)(false))) # Нет