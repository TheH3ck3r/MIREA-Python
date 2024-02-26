def task_1(n: int, m: int, a: int):
  sum_3 = 1
  for c in range(1, a + 1):
    sum_2 = 1
    for j in range(1, m + 1):
      sum_1 = 0
      for i in range(1, n + 1):
        sum_1 += (((28 * (c ** 2)) ** 6) / 5) + 16 * (((j ** 3 / 44) + (i ** 2)) ** 5)
      sum_2 *= sum_1
    sum_3 *= sum_2
  return sum_3

print(task_1(n=4, m=2, a=8))
