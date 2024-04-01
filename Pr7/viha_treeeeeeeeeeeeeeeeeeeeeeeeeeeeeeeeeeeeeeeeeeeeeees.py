
def task26(x: int, y: int):
    return (((x << 2) + (y >> 5)) - (y - 7 if y > 3 else y)) - (3 if y > 8 else x)

def task27(x: int, y: int):
    return ((y + (9 if x < 5 else x)) - (y | 8)) + (x if y < 10 else 3)

def task28(x: int, y: int):
    return ((x - 3) - (x // 9 if y <= 1 else x >> 7)) + 7

def task29(x: int, y: int):
    return (((y * 8) + 5) + (x >> 1)) - (y >> 1 if x <= 1 else y % 10)

def task30(x: int, y: int):
    return ((2 - (y % 7)) - (y - 1 if x != 8 else 7)) + 5

# ---------------------------------------------------

print("task26:",task26(3, 1))

print("task27:",task27(1, 3))

print("task28:",task28(2, 5))

print("task29:",task29(5, 1))

print("task30:",task30(2, 3))