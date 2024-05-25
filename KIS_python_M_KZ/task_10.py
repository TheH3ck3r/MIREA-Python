def main(input_table):
    transformed_table = []
    for row in input_table:
        score = str(round(row[0], 2))
        if len(score) == 3:
            score += '0'
        email, name = str(row[1]).split(';')
        email = str(email).split('@')[0]
        name_parts = str(name).split()
        last_name = name_parts[2]
        first_initial = name_parts[0][0]
        middle_initial = name_parts[1][0]
        full_name = f"{last_name}, {first_initial}.{middle_initial}."
        transformed_table.append([score, email, full_name])
    
    transformed_table.sort(key=lambda x: x[1])
    
    transposed_table = list(map(list, zip(*transformed_table)))
    
    return transposed_table

input_table_1 = [
    [0.380, "ramil_61@yandex.ru;Рамиль Р. Шемин"],
    [0.224, "sevasman27@gmail.com;Валерий А. Севашман"],
    [0.033, "funogan54@yandex.ru;Марат Е. Фуногян"],
]

input_table_2 = [
    [0.802, "lalman6@yahoo.com;Тимур Б. Лалман"],
    [0.001, "ladberg12@gmail.com;Савва Ч. Ладберг"],
    [0.997, "timofej1@yahoo.com;Тимофей А. Мирян"],
    [0.177, "zizocak64@rambler.ru;Эмиль М. Цицочак"],
]

if __name__ == '__main__':
    print(main(input_table_1))
    print(main(input_table_2))

