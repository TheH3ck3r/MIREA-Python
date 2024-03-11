import numpy as np
import matplotlib.pyplot as plt

def generate_sprite():
    sprite = np.random.randint(0, 2, (5, 5))
    sprite = np.maximum(sprite, sprite[:, ::-1])
    return sprite

def generate_sprite_map(cols, rows, padding):
    sprite_width = 5 + padding
    sprite_height = 5 + padding
    sprite_map = np.zeros((sprite_height * rows - padding, sprite_width * cols - padding)) 
    for i in range(rows):
        start_row = i * sprite_height
        end_row = start_row + 5
        for j in range(cols):
            start_col = j * sprite_width
            end_col = start_col + 5
            sprite_map[start_row:end_row, start_col:end_col] = generate_sprite()
    return sprite_map

sprite_map = generate_sprite_map(cols=20, rows=10, padding=5) 
plt.imshow(sprite_map, cmap='gray', interpolation='nearest')
plt.show()
