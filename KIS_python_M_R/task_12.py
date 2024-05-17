from struct import unpack_from, calcsize


class Types:
    double = 'd'

    int32 = 'i'
    uint32 = 'I'

    int16 = 'h'
    uint16 = 'H'

    int8 = 'b'
    uint8 = 'B'

    int64 = 'q'
    uint64 = 'Q'

    char = 's'  # или 'c'

    float = 'f'


class BinaryReader:
    def __init__(self, data, offset, order='<'):
        self.data = data
        self.offset = offset
        self.order = order

    def jump_to(self, offset):
        reader = BinaryReader(self.data, offset, self.order)
        return reader

    def read(self, frmt):
        data = unpack_from(self.order + frmt, self.data, self.offset)
        self.offset += calcsize(frmt)
        return data[0]


def read_e(reader):
    e1 = [reader.read(Types.uint64) for _ in range(6)]
    e2 = reader.read(Types.int8)
    e3 = reader.read(Types.int16)
    return dict(E1=e1, E2=e2, E3=e3)


def read_d(reader):
    d1_size = reader.read(Types.uint16)
    d1_offset = reader.read(Types.uint32)
    d1_reader = reader.jump_to(d1_offset)
    d1 = [d1_reader.read(Types.float) for _ in range(d1_size)]

    d2 = reader.read(Types.int8)
    return dict(D1=d1, D2=d2)


def read_c(reader):
    c1 = reader.read(Types.uint64)
    c2 = reader.read(Types.uint16)
    return dict(C1=c1, C2=c2)


def read_b(reader):
    b1 = reader.read(Types.float)
    b2 = b''.join([reader.read(Types.char) for _ in range(2)]).decode()
    b3 = reader.read(Types.uint8)
    b4 = reader.read(Types.float)
    b5 = read_c(reader)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5)


def read_a(reader):
    b_offset = reader.read(Types.uint32)
    b_reader = reader.jump_to(b_offset)
    a1 = [read_b(b_reader) for _ in range(2)]

    a2 = reader.read(Types.int8)
    a3 = read_d(reader)
    a4 = read_e(reader)
    a5 = reader.read(Types.double)
    a6 = reader.read(Types.int16)
    a7 = reader.read(Types.int64)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def main(data):
    return read_a(BinaryReader(data, 5))


print(main(b'ZZMT\xbeZ\x00\x00\x00o\x00\x00\x00\xdb\x02\x00\x84\x00\x00\x00\x19V\xa2F'
           b'\x96\xbf.%\xd8R\xc8\x89\x9f\xf9\x19S\xc0imJ\xdd\x93"\x8ay\xedj6t8]\xda'
           b'\xd3\xc94gJ\x05\x8fqe\x00\x88\xa0\x8fQ\xdbhW\x8d^k\xe0\x00\xdbB'
           b'\xf5\xd8\xc5\xbf\xa2t}d\x7f\x1f\x8b\xcel\xd9Qh\xb7\xbelv\xf8\x06\xf8\xfb'
           b'>\xad\xe6\x06\x06"]\x80\xc5\xd6\x80\x1ad{?oq\xe1\x92S\x1b\xbf}\xc6'
           b'\xd86\x18\xff\xbf\x7f\xbd\xd5\x8aj\xec>\xad\xd5\xd0\xbe'))

print("\n-------------------------------------------------------------------------------------------\n")

print(main(b'ZZMT\xbeZ\x00\x00\x00o\x00\x00\x00\x95\x04\x00\x84\x00\x00\x00'
           b'\x9f\xb8\xf0\x15U\xe6\x9b\xd22\xea\xef\xc3\x02\xb8\xd6\x02\x92>\x7f\xfe'
           b'\x9f\x96c\x00\x13\xa7\xca\xa0\xbc\xd8HY\xe9\xd3\xa9\x98j\xe1\x81\x92'
           b"4\x14L\xc4{ET\x0e\xf5\x1a\x19\xfd`\xa6o\x86\x13\xff\xe0\xbf\xbd\x93]'"
           b'\xd7\x8d\t1\x8fh\x01\x8a\x17\xbfwm.@\xf3{\xbdf\xb0\x0b\x8b\x90T,'
           b"\xb5\xed\xab\x99]\x1b\xbfaq'\x94\xedv\xbf$\xd0\xcf>\x01^\x86\xb5\xfc\xe7"
           b"\xe7q'\xbf,V\x11\xbf\xd6=1;d\x11N\xbe"))
