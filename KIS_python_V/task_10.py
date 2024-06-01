def remove_duplicate_columns(input_table):
    seen = set()
    unique_columns = []
    for row in input_table:
        unique_row = []
        for value in row:
            if value not in seen:
                seen.add(value)
                unique_row.append(value)
            else:
                unique_row.append(None)
        unique_columns.append(unique_row)
    return unique_columns

def remove_empty_columns(unique_columns):
    unique_columns = list(map(list, zip(*unique_columns)))
    non_empty_columns = [col for col in unique_columns if any(val is not None for val in col)]
    non_empty_columns = list(map(list, zip(*non_empty_columns)))
    return non_empty_columns

def split_column(non_empty_columns, split_index=0):
    for row in non_empty_columns:
        if row[split_index] is not None:
            phone, name = row[split_index].split('!')
            row[split_index] = phone
            row.append(name)
    return non_empty_columns

def transform_row(row):
    name_parts = row[-1].split()
    transformed_name = f"{name_parts[1]} {name_parts[0]}"
    
    score = round(float(row[1]), 1)
    
    email = row[3].split('@')[0]
    
    phone = row[0][-9:]
    formatted_phone = f"{phone[:3]}-{phone[3:5]}-{phone[5:]}"
    
    return [transformed_name, f"{score:.1f}", email, formatted_phone]

def transform_table(input_table):
    unique_columns = remove_duplicate_columns(input_table)
    non_empty_columns = remove_empty_columns(unique_columns)
    split_columns = split_column(non_empty_columns)
    
    transformed_table = [transform_row(row) for row in split_columns]
    transformed_table.sort(key=lambda x: x[1])  # сортировка по баллу
    
    transposed_table = list(map(list, zip(*transformed_table)))
    
    return transposed_table

# Пример использования:
input_table = [
    ["+78461967740!Вочонберг Игорь", "0.5691", None, "voconberg48@yandex.ru", "0.5691"],
    ["+77649968035!Фишебяк Данил", "0.3252", None, "fisebak92@yahoo.com", "0.3252"],
    ["+75593897421!Шевакли Игнат", "0.7664", None, "sevakli19@gmail.com", "0.7664"],
    ["+79406370337!Золян Рустам", "0.1996", None, "rustam97@yandex.ru", "0.1996"],
]

output_table = transform_table(input_table)
print(output_table)
