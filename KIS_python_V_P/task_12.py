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
    e1 = reader.read(Types.int8)
    e2 = reader.read(Types.uint64)
    e3 = reader.read(Types.double)
    return dict(E1=e1, E2=e2, E3=e3)


def read_d(reader):
    d1 = reader.read(Types.uint16)
    d2 = reader.read(Types.uint32)
    d3 = [reader.read(Types.uint16) for _ in range(6)]
    d4 = reader.read(Types.uint16)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4)


def read_c(reader):
    c1 = reader.read(Types.double)
    c2 = reader.read(Types.double)
    c3 = reader.read(Types.int32)
    c4 = b''.join([reader.read(Types.char) for _ in range(7)]).decode()
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_b(reader):
    b1 = reader.read(Types.int32)
    b2 = reader.read(Types.int16)
    b3 = reader.read(Types.int64)
    b4 = reader.read(Types.int8)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4)


def read_a(reader):
    b_offset = reader.read(Types.uint32)
    b_reader = reader.jump_to(b_offset)
    a1 = read_b(b_reader)

    a2 = reader.read(Types.int64)

    a3_size = reader.read(Types.uint32)
    a3_offset = reader.read(Types.uint16)
    a3_reader = reader.jump_to(a3_offset)
    a3 = [read_c(a3_reader) for _ in range(a3_size)]

    a4 = reader.read(Types.float)
    a5 = reader.read(Types.float)
    a6 = reader.read(Types.int64)

    a7 = [read_d(reader) for _ in range(2)]

    e_offset = reader.read(Types.uint16)
    e_reader = reader.jump_to(e_offset)
    a8 = read_e(e_reader)

    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8)


def main(data):
    return read_a(BinaryReader(data, 3))


print(main(b'VKHO\x00\x00\x00\x99\x0fIQ\t\xac\xfe\r\x02\x00\x00\x00^\x00|3\x12?i\xae\xba'
           b'>_\xfa\x8f\x00V\xb7\x9b8\xbdJ\xe6\x95\xa4\x97\x13\x06z\xc6\xc85Qu\xe7'
           b'x\xb6e\xe2_\xab\xc0\x05Pm\xf4\x81\x7fchb>\xa0\xea\x99%+\x1fz\xf6\x94\x00\xa4'
           b'\x81\xc4\x99V\xa0\x0c\x91N\xef~\xf3\xa3U\x8d\xbe\xb3\xbc\x0b4\xf6\xea?dt'
           b'N\xd2H\xab\xd9?\x87\xadAOagvlttfT\xa9\xcbp5\xc4\xec\xbfX\x9f\x97{\x10\r\xe3'
           b'?\x148\x1a\xd9efyhobu\xf7\xbb\xa9\xa6v7\xcf\xc7,X\x10\xc1\x19\xf1\x9d\xd2?'))
