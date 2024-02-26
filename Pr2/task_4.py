def task_4(y: list, z: list):
    n = len(y)
    new_list = []
    for i in range(n):
        new_list.append(((y[i]-z[i])**2)**0.5)
    max_value = new_list[0]
    for i in range(n):
        if max_value <= new_list[i]:
            max_value = new_list[i]
    return max_value

print(task_4(y=[1, 0.5, 1], z=[0.5, 2, 1]))
