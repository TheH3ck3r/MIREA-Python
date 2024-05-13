def main(z):
    numerator = 83 * (37 * z ** 3) ** 6 + 96 * z ** 23
    denominator = z ** 7 - 57 * z ** 6
    sqrt_value = (numerator / denominator) ** 0.5
    return z ** 2 - 1 + sqrt_value
