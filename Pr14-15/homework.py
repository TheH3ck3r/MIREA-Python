# 1.1
def power(x,y):
  return x ** y

print("1.1:", power(2,3))


# 1.2
def power(x):
  def p(y):
    return x**y
  return p

print("1.2:", power(2)(3))


#1.3
power = lambda x: lambda y: x**y

print("1.3:", power(2)(3))


#2.1
deriv = lambda f: lambda x: (f(x + 10**-6) - f(x)) / 10**-6
result = deriv(lambda x: x ** 3)(5)
print("2.1:", result)


#2.2
deriv = lambda f: lambda x: (f(x + 10**-6) - f(x - 10**-6)) / (2 * (10**-6))
result = deriv(lambda x: x ** 3)(5)
print("2.2:", result)


#3.1
I = lambda x: x
K = lambda x: lambda y: x
KI = lambda x: lambda y: y

С = lambda f: lambda a: lambda b: f(b)(a)

M = lambda x: x(x)

power = lambda x: lambda y: x ** y

print("\n------3.1------")
print(I(42))
print(K(1)(2))
print(KI(1)(2))
# print(C(C(power))(2)(5)) У меня он на С ругается почему-то, так что оставлю в коментарии. А так всё должно работать (в этом номере)
print(M(lambda x: 42))
print("---------------")


#3.2
K = lambda x: lambda y: x
KI = lambda x: lambda y: y

Vireo = lambda x: lambda y: lambda f: f(x)(y)

pair = Vireo
my_tuple = pair(3)(4)
print("\n------3.2------")
print(my_tuple(K))
print(my_tuple(KI))
print("---------------")


#4.1
true = lambda x: lambda y: x
false = lambda x: lambda y: y

stringify = lambda p: p("Да")("Нет")

print("\n------4.1------")
print(stringify(true))
print(stringify(false))
print("---------------")


#4.2
true = lambda x: lambda y: x
false = lambda x: lambda y: y

inv = lambda p: lambda x: lambda y: p(y)(x)
stringify = lambda p: p("Да")("Нет")

print("\n------4.2------")
print(stringify(inv(true))) # Нет
print(stringify(inv(inv(inv(false))))) # Да
print("---------------\n")


#4.3
def if_then_else(condition):
    return lambda then_branch: lambda else_branch: condition(then_branch)(else_branch)


print("4.3:", if_then_else(lambda x: lambda y: x)("Истина")("Ложь"))


#4.4
true = lambda x: lambda y: x
false = lambda x: lambda y: y

stringify = lambda p: p("Да")("Нет")

K = lambda x: lambda y: x

def either(x):
    return lambda y: K(x)(y)

print("\n------4.4------")
print(stringify(either(true)(false)))  # Да
print(stringify(either(false)(false)))  # Нет
print("---------------")


#4.5
true = lambda x: lambda y: x
false = lambda x: lambda y: y


both = lambda p: lambda q: p(q)(p)


def stringify(boolean_function):
    return "Да" if boolean_function == true else "Нет"


print("\n------4.5------")
print(stringify(both(true)(true)))   # Да
print(stringify(both(false)(true)))  # Нет
print(stringify(both(true)(false)))  # Нет
print(stringify(both(false)(false))) # Нет
print("---------------")

#4.6
true = lambda x: lambda y: x
false = lambda x: lambda y: y

stringify = lambda b: "Да" if b(true)(false) == true else "Нет"
inv = lambda x: x(false)(true)

eq = lambda p: lambda q: p(q)(inv(q))
print("\n------4.6------")
print(stringify(eq(true)(true)))  # Да
print(stringify(eq(false)(true))) # Нет
print(stringify(eq(true)(false))) # Нет
print(stringify(eq(false)(false))) # Да
print("---------------\n")


#4.7
# Z = lambda f: (lambda x: f(x(x)))(lambda x: f(x(x)))          Он не особо работает
# fact = Z(lambda f: lambda n: 1 if n == 0 else n * f(n - 1))

# print("4.7: ", fact(5))


#4.8
Z = lambda g: (lambda x: g(lambda v: x(x)(v))) \
            (lambda x: g(lambda v: x(x)(v)))

fact = Z(lambda f: lambda n: 1 if n == 0 else n * f(n - 1))

result = fact(5)

print("4.8: ", result)