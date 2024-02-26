import math

def task_3 (y: list, z: list):
  result = 0
  for i in range(len(y)):
    result += math.fabs(y[i] - z[i])
  return result

print(task_3(y=[1, 0.5, 1], z=[0.5, 2, 1]))