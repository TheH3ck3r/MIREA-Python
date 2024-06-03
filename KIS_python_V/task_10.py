import copy


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
    parse_object = (str(massive[0])).split(" ")
    massive[0] = f'{parse_object[len(parse_object)-1]} {parse_object[0]}'
    massive[1] = f'{round(float(massive[1]), 1)}'
    parse_object = (str(massive[2])).split('@')
    massive[2] = parse_object[0]
    return massive


def transpose(massive: list):
    answer = [
        [],
        [],
        [],
        [],
    ]
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            answer[j].append(massive[i][j])

    return answer


def main(massives):
    new_massives = copy.deepcopy(massives)
    for i in range(len(new_massives)):
        new_massives[i] = checking_for_copies(massive=new_massives[i])
    for i in range(len(new_massives)):
        new_massives[i] = [
            element for element in new_massives[i] if element is not None
        ]
    for i in range(len(new_massives)):
        another_mass = (new_massives[i][0]).split("!")
        new_massives[i][0] = another_mass[1]
        new_massives[i].insert(len(new_massives[i]),
                               f'{"".join(another_mass[0][5:8])}'
                               f'-{"".join(another_mass[0][8:10])}'
                               f'-{"".join(another_mass[0][10:12])}')
    for i in range(len(new_massives)):
        new_massives[i] = prettify(massive=new_massives[i])

    new_massives.sort(key=lambda x: x[2])

    return transpose(new_massives)
