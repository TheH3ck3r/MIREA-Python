import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

file = pd.read_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_2/GAMES.csv', delimiter=';')

df = pd.DataFrame(file)

another_dict = list(df.iloc[:, 3])

all_date_variants = set(another_dict)

count = Counter(another_dict)

values_dict = count.values()
keys_dict = count.keys()

index = [0, 1, 2, 3, 4]
values = [5, 7, 3, 4, 6]
plt.bar(list(keys_dict), list(values_dict))
plt.show()
