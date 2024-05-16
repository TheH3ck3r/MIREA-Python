import copy
import datetime


def checking_for_copies(massive: list):
    seen = []
    delete_to = []
    for i in range(len(massive)):
        if massive[i] not in seen:
            seen.append(massive[i])
        else:
            delete_to.append(i)
    delete_to = sorted(delete_to, reverse=True)
    for i in delete_to:
        massive.pop(i)
    return massive


def prettify(massive: list):
    parse_object = (str(massive[0])).split("[at]")
    massive[0] = parse_object[len(parse_object) - 1]
    massive[1] = datetime.datetime.strftime(
        datetime.datetime.strptime(massive[1], "%d/%m/%Y"), "%d-%m-%y"
    )
    massive[2] = 'false' if int(massive[2]) == 0 else 'true'
    massive[3] = str(round(float(massive[3]), 1))
    return massive


def main(massives):
    new_massives = copy.deepcopy(massives)

    for i in range(len(new_massives)):
        new_massives[i] = checking_for_copies(massive=new_massives[i])
    new_massives = checking_for_copies(massive=new_massives)
    for _ in new_massives:
        if None in _:
            new_massives.remove(_)

    for i in range(len(new_massives)):
        new_massives[i] = prettify(massive=new_massives[i])
    return new_massives


s = [
    ['bozikin46[at]rambler.ru', '02/02/2001', '0', '0.87', '0.87'],
    [None, None, None, None, None],
    ['bozikin46[at]rambler.ru', '02/02/2001', '0', '0.87', '0.87'],
    ['lesucman1[at]yahoo.com', '24/12/2001', '0', '0.49', '0.49'],
    ['busev76[at]yandex.ru', '25/01/1999', '1', '0.11', '0.11']
]

if __name__ == '__main__':
    print(main(s))
