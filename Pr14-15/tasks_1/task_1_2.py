def power(x):
  def p(y):
    return x**y
  return p

print(power(2)(3))