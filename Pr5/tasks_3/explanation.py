import csv
import datetime
import pandas as pd
import matplotlib.pyplot as plt

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')

def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

# Загрузка данных
messages = load_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_3/messages.csv')
checks = load_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_3/checks.csv')
statuses = load_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_3/statuses.csv')

# Преобразование времени в формат datetime
messages = [(int(m[1]), parse_time(m[4])) for m in messages]
checks = [(int(c[1]), parse_time(c[2])) for c in checks]
statuses = [(int(s[1]), parse_time(s[3])) for s in statuses]

# Преобразование данных в DataFrame для удобства работы
messages_df = pd.DataFrame(messages, columns=['task', 'time'])
checks_df = pd.DataFrame(checks, columns=['message_id', 'time'])
statuses_df = pd.DataFrame(statuses, columns=['task', 'time'])

# ------------------------------------------------------------------------------------------------------

# task_3.1

# Объединение данных по времени и подсчет количества событий по дням недели
activity = pd.concat([messages_df, checks_df, statuses_df])
activity['day_of_week'] = activity['time'].dt.dayofweek
activity_count = activity.groupby('day_of_week').size()

# Построение графика
plt.figure(figsize=(10, 6))
activity_count.plot(kind='bar', color='skyblue')
plt.title('Распределение активности студентов по дням недели')
plt.xlabel('День недели')
plt.ylabel('Количество событий')
plt.xticks(range(7), ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'], rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ------------------------------------------------------------------------------------------------------

# task_3.2

# Объединение данных по времени и подсчет количества событий по дням недели
activity = pd.concat([messages_df, checks_df, statuses_df])
activity['day_of_week'] = activity['time'].dt.dayofweek
activity_count = activity.groupby('day_of_week').size()

# Функция для определения временного интервала по времени
def get_time_interval(hour):
    if 6 <= hour < 12:
        return 'Утро'
    elif 12 <= hour < 18:
        return 'День'
    elif 18 <= hour < 24:
        return 'Вечер'
    else:
        return 'Ночь'

# Добавление временного интервала в данные
activity['hour'] = activity['time'].dt.hour
activity['time_interval'] = activity['hour'].apply(get_time_interval)

# Подсчет количества событий по временным интервалам
activity_count_by_time = activity.groupby('time_interval').size()

# Построение графика
plt.figure(figsize=(8, 6))
activity_count_by_time.plot(kind='bar', color='lightgreen')
plt.title('Распределение активности студентов по времени суток')
plt.xlabel('Временной интервал')
plt.ylabel('Количество событий')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# ------------------------------------------------------------------------------------------------------

# task_3.3

# Подсчет количества сообщений по каждой задаче
messages_count_per_task = messages_df.groupby('task').size()

# Подсчет среднего количества сообщений по задачам
average_messages_per_task = messages_count_per_task.mean()
print("Среднее количество сообщений по каждой задаче:", average_messages_per_task)
