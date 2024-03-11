# task_4.1.py
import numpy as np
import matplotlib.pyplot as plt

# Создание случайного спрайта 5x5 с использованием симметрии
sprite = np.random.randint(0, 2, (5, 5))

# Горизонтальное зеркальное отражение спрайта
sprite = np.maximum(sprite, sprite[:, ::-1])

# Вывод спрайта с помощью imshow()
plt.imshow(sprite, cmap='gray', interpolation='nearest')
plt.axis('off')  # Отключение осей координат
plt.show()

# ------------------------------------------------------------------------------------------------------

# task_4.2.py
import numpy as np
import matplotlib.pyplot as plt

def generate_sprite():
    # Функция генерации случайного спрайта размером 5x5 пикселей
    sprite = np.random.randint(0, 2, (5, 5))  # Создаем спрайт с рандомными значениями 0 и 1
    sprite = np.maximum(sprite, sprite[:, ::-1])  # Делаем спрайт симметричным
    return sprite

def generate_sprite_map(n, padding):
    # Функция генерации карты спрайтов
    sprite_width = 5 + padding  # Ширина спрайта с учетом отступа
    sprite_height = 5 + padding  # Высота спрайта с учетом отступа
    # Создаем пустой массив для карты спрайтов
    sprite_map = np.zeros((sprite_height * n - padding, sprite_width * n - padding)) 
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
plt.imshow(sprite_map, cmap='gray', interpolation='nearest')
plt.show()
