import math

def task_6 (y: list, z: list, h: int):
  result = 0
  for i in range(len(y)):
    result += math.fabs(y[i] - z[i]) ** h
  return result ** (1 / h)

print(task_6(y=[1, 0.5, 1], z=[0.5, 2, 1], h=5))