def main(fields):
    Q1, Q2, Q4 = map(int, fields)
    result = 0
    result |= (Q1 & 0xFF)
    result |= (Q2 & 0xF) << 8
    result |= (Q4 & 0x3F) << 20
    return result

print(main(('154', '8', '46')))
print(main(('75', '15', '30')))
print(main(('158', '5', '62')))
print(main(('246', '0', '2')))