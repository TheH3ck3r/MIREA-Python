def main(z):
    decoded_value = int(z, 16)

    value1 = decoded_value & ((1 << 10) - 1)
    value3 = (decoded_value >> 18) & ((1 << 6) - 1)
    value4 = (decoded_value >> 24) & ((1 << 4) - 1)

    result = (
        (value1 << 18)
        | (value4 << 14)
        | value3
    )

    return str(result)

if __name__ == '__main__':
    print(main('0x9807158'))