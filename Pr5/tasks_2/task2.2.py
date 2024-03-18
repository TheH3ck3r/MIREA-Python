import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = pd.read_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_2/GAMES.csv', delimiter=';')

df = pd.DataFrame(file)

column_4_data = df.iloc[:, 3]

column_2_data = df.iloc[:, 1]

game_type = set(list(column_2_data))
dates = set(list(column_4_data))

concatenated_data = pd.concat([column_2_data, column_4_data], axis=1)

list_to_check = concatenated_data.values.tolist()

new_object = {}

for game in game_type:
    new_object[game] = {}
    for date in dates:
        new_object[game][date] = 0


for i in range(len(list_to_check)):
    new_object[list_to_check[i][0]][list_to_check[i][1]] += 1

df = pd.DataFrame(new_object)

data = {}

x = np.arange(len(data))
df.plot(stacked=True)
plt.show()
