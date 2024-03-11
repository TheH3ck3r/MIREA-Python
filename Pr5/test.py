import numpy as np
import matplotlib.pyplot as plt

# Цвета спрайтов в формате RGB
colors = {
    '1D2B53': [29, 43, 83],
    '7E2553': [126, 37, 83],
    '008751': [0, 135, 81],
    'AB5236': [171, 82, 54],
    '5F574F': [95, 87, 79],
    'C2C3C7': [194, 195, 199],
    'FFF1E8': [255, 241, 232],
    'FF004D': [255, 0, 77],
    'FFA300': [255, 163, 0],
    'FFEC27': [255, 236, 39],
    '00E436': [0, 228, 54],
    '29ADFF': [41, 173, 255],
    '83769C': [131, 118, 156],
    'FF77A8': [255, 119, 168],
    'FFCCAA': [255, 204, 170]
}

def generate_sprite():
    # Функция генерации случайного спрайта размером 5x5 пикселей с выбранным цветом
    color_code = np.random.choice(list(colors.keys()))  # Выбираем случайный цвет из палитры
    color_rgb = colors[color_code]  # Получаем RGB-значения для выбранного цвета
    sprite = np.array([color_rgb] * 5)  # Создаем спрайт, заполняя все строки одним цветом
    return sprite

def generate_sprite_map(n, padding):
    # Функция генерации карты спрайтов
    sprite_width = 5 + padding  # Ширина спрайта с учетом отступа
    sprite_height = 5 + padding  # Высота спрайта с учетом отступа
    # Создаем пустой массив для карты спрайтов
    sprite_map = np.zeros((sprite_height * n - padding, sprite_width * n - padding, 3), dtype=int) 
    for i in range(n):
        start_row = i * sprite_height  # Начальная строка для размещения спрайта
        end_row = start_row + 5  # Конечная строка для размещения спрайта
        for j in range(n):
            start_col = j * sprite_width  # Начальный столбец для размещения спрайта
            end_col = start_col + 5  # Конечный столбец для размещения спрайта
            sprite_map[start_row:end_row, start_col:end_col] = generate_sprite()  # Размещаем спрайт на карте
    return sprite_map

# Генерируем карту спрайтов размером 10x10 со смещением между спрайтами в 5 пикселей
sprite_map = generate_sprite_map(10, padding=5) 
# Визуализируем карту спрайтов
plt.imshow(sprite_map)
plt.show()
