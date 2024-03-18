import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

messages = load_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_3/messages.csv')
checks = load_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_3/checks.csv')
statuses = load_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_3/statuses.csv')

messages = [(int(m[1]), parse_time(m[4])) for m in messages]
checks = [(int(c[1]), parse_time(c[2])) for c in checks]
statuses = [(int(s[1]), parse_time(s[3])) for s in statuses]

messages_df = pd.DataFrame(messages, columns=['task', 'time'])
checks_df = pd.DataFrame(checks, columns=['message_id', 'time'])
statuses_df = pd.DataFrame(statuses, columns=['task', 'time'])

messages_count_per_task = messages_df.groupby('task').size()

average_messages_per_task = messages_count_per_task.mean()
print("Среднее количество сообщений по каждой задаче:", average_messages_per_task)
