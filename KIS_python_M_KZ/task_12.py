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


def read_f(reader):
    f1 = reader.read(Types.int32)

    f2 = [reader.read(Types.int8) for _ in range(6)]

    f3 = reader.read(Types.uint16)

    f4 = reader.read(Types.int64)

    f5_size = reader.read(Types.uint16)
    f5_offset = reader.read(Types.uint16)
    f5_reader = reader.jump_to(f5_offset)
    f5 = [f5_reader.read(Types.uint16) for _ in range(f5_size)]

    return dict(F1=f1, F2=f2, F3=f3, F4=f4, F5=f5)


def read_e(reader):
    e1 = reader.read(Types.int32)
    e2 = reader.read(Types.float)
    e3 = reader.read(Types.uint16)
    e4 = [reader.read(Types.uint8) for _ in range(4)]
    e5 = reader.read(Types.uint32)
    e6 = reader.read(Types.double)
    return dict(E1=e1, E2=e2, E3=e3, E4=e4, E5=e5, E6=e6)


def read_d(reader):
    d1 = reader.read(Types.int64)
    d2 = reader.read(Types.uint32)
    d3 = reader.read(Types.int16)
    d4 = reader.read(Types.uint64)
    d5 = reader.read(Types.uint32)

    d6_size = reader.read(Types.uint16)
    d6_offset = reader.read(Types.uint32)
    d6_reader = reader.jump_to(d6_offset)
    d6 = [read_e(d6_reader) for _ in range(d6_size)]

    d7 = reader.read(Types.float)

    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7)


def read_c(reader):
    d_offset = reader.read(Types.uint32)
    d_reader = reader.jump_to(d_offset)
    c1 = read_d(d_reader)

    c2 = reader.read(Types.int32)
    c3 = read_f(reader)
    c4 = reader.read(Types.uint16)
    c5 = reader.read(Types.int8)
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5)


def read_b(reader):
    b1 = reader.read(Types.uint16)
    b2 = reader.read(Types.uint8)
    return dict(B1=b1, B2=b2)


def read_a(reader):
    a1 = reader.read(Types.int32)
    a2 = read_b(reader)

    c_offset = reader.read(Types.uint16)
    c_reader = reader.jump_to(c_offset)
    a3 = read_c(c_reader)
    return dict(A1=a1, A2=a2, A3=a3)


def main(data):
    return read_a(BinaryReader(data, 4))


print(main(b'PBJH\xb3\x7f\x0c\xac\xd4Jek\x00\xd2\xe9N+\xa6\xe1k?\xdah\xcd\x80\xa2BJ'
           b'\xfdq\xb14\xb8-\xc2\xeb\x89\xd0?\x19\xed\xea\xce\x85JY>M\x8e+n[\xc8\xca0\x0c'
           b'"\x1c)\x0bm\xc8\xf8\xef\xbfC.\xfa\x7f&Q\xba\xa5\xde\xfa\x02\x05\x14z\x1f'
           b'k\xc1\xfd\xf9\x7f\x8e\x8f\x9fA\x94\xb8\x02\x00\r\x00\x00\x007i\x8e'
           b'\xbe\xe1y\x96\xc8\xedAA\x00\x00\x00\xc7\x04\xe3\xf9;\xd4\x12\x0ew'
           b'/\xbc\xb2\xd9\xb1\x1f\xfb\xd8\xa1\xb3gM\x87}@\x03\x00e\x00V\x91!'))