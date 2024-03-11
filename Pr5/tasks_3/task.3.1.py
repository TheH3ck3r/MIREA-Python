import csv
import datetime

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))

# id, task, variant, group, time
messages = load_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_3/messages.csv')

# id, message_id, time, status
checks = load_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_3/checks.csv')

# TODO: Добавить данные в файл statuses.csv
# task, variant, group, time, status, achievements
# statuses = load_csv('/home/thehacker/code/MIREA/4_sem/Python/MIREA-Python/Pr5/tasks_3/statuses.csv')