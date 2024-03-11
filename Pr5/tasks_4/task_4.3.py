import numpy as np
import matplotlib.pyplot as plt

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
