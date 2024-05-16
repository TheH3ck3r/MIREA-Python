def main(z):
    decoded_value = int(z)

    field1_value = decoded_value & ((1 << 10) - 1)
    field2_value = (decoded_value >> 10) & ((1 << 9) - 1)
    field4_value = (decoded_value >> 29) & ((1 << 4) - 1)
    field5_value = (decoded_value >> 33) & ((1 << 1) - 1)
    field6_value = (decoded_value >> 34) & ((1 << 8) - 1)

    real_result = (
        (field1_value << 31)
        | (field2_value << 12)
        | (field4_value << 8)
        | (field5_value << 41)
        | field6_value
    )

    return hex(real_result)


if __name__ == '__main__':
    print(main(z='2582908600056'))
    print(main(z='1675040462978'))
    print(main(z='608090984524'))
    print(main(z='589740522906'))
