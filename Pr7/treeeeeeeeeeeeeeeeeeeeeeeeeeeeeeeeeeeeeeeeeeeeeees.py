
def task26(x: int, y: int):
    return ((y + (y if y < 6 else 1)) - (8 if y > 3 else y - 6)) - (x // 6)

def task27(x: int, y: int):
    return (((x * 8) + (y if x > 9 else x & 6)) - (y | 1 if y <= 6 else 10)) + (3 if x > 2 else y)

def task28(x: int, y: int):
    return (((y | 7 if x != 8 else y) + (x * 3 if x >= 3 else y)) + (6 if y <= 4 else x / 9)) - (x - 10 if x >= 5 else y >> 4)

def task29(x: int, y: int):
    return (((x << 5) - (y if x != 7 else 10)) - y) - (4 if y != 2 else x)

def task30(x: int, y: int):
    return (((1 if y > 2 else y << 4) - 5) + x) + (7 if y <= 10 else 2)

# ---------------------------------------------------

print("task26:",task26(5, 5))

print("task27:",task27(2, 4))

print("task28:",task28(3, 2))

print("task29:",task29(1, 2))

print("task30:",task30(5, 1))