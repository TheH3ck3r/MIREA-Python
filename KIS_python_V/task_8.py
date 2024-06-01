def main(n):
    decoded_value = int(n)

    Z1 = decoded_value & ((1 << 7) - 1)
    Z2 = (decoded_value >> 7) & ((1 << 9) - 1)
    Z3 = (decoded_value >> 16) & ((1 << 1) - 1)
    Z4 = (decoded_value >> 17) & ((1 << 9) - 1)
    Z5 = (decoded_value >> 26) & ((1 << 7) - 1)
    Z6 = (decoded_value >> 33) & ((1 << 2) - 1)

    return (Z1, Z2, Z3, Z4, Z5, Z6)

print(main(721758738))    # (18, 84, 1, 386, 10, 0)
print(main(16263148667))  # (123, 488, 1, 173, 114, 1)
print(main(25974227981))  # (13, 136, 1, 23, 3, 3)
print(main(14777746397))  # (93, 263, 0, 105, 92, 1)
