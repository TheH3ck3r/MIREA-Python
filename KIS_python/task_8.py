def main(n):
    result_object = {}

    decoded_value = int(n)

    field1_value = decoded_value & ((1 << 3) - 1)
    field2_value = (decoded_value >> 3) & ((1 << 9) - 1)
    field3_value = (decoded_value >> 12) & ((1 << 8) - 1)
    field4_value = (decoded_value >> 20) & ((1 << 2) - 1)

    result_object['D1'] = field1_value
    result_object['D2'] = field2_value
    result_object['D3'] = field3_value
    result_object['D4'] = field4_value
    return result_object

if __name__ == '__main__':
    print(main("4140168"))