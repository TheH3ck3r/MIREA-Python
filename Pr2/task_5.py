def task_5 (y: list, z: list):
  result = 0
  for i in range(len(y)):
    result += (y[i]-z[i]) ** 2
  return result

print(task_5(y=[1, 0.5, 1], z=[0.5, 2, 1]))