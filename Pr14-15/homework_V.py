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
