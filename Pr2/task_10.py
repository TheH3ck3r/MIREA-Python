def task_10(a: str, b: str, i: int, j: int):
  if i == 0 or j == 0:
    return max(i, j)
  elif a[i - 1] == b[j - 1]:
    return task_10(a=a, b=b, i=i-1, j=j-1)
  else:
    return 1 + min(
      task_10(a=a, b=b, i=i, j=j-1),
      task_10(a=a, b=b, i=i-1, j=j),
      task_10(a=a, b=b, i=i-1, j=j-1))



a_list = ['Hello, world!', 'Hello, world!', 'I love Python', '100101']
b_list = ['Goodbye, world!', 'Bye, world!', 'I like Python', '100011']
n = len(a_list)
for number in range(n):
  print(task_10(a=a_list[number], b=b_list[number], i=len(a_list[number]), j=len(b_list[number])))
