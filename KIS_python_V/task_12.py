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


def read_d(reader):
    d1 = reader.read(Types.float)
    d2 = [reader.read(Types.float) for _ in range(7)]
    return dict(D1=d1, D2=d2)


def read_c(reader):
    c1 = reader.read(Types.int16)
    c2 = reader.read(Types.uint32)
    return dict(C1=c1, C2=c2)


def read_b(reader):
    b1 = reader.read(Types.uint8)
    b2 = reader.read(Types.float)
    b3 = reader.read(Types.uint32)

    b4_size = reader.read(Types.uint16)
    b4_offset = reader.read(Types.uint32)
    b4_reader = reader.jump_to(b4_offset)
    b4 = b''.join([b4_reader.read(Types.char)
                   for _ in range(b4_size)]).decode()

    b5 = reader.read(Types.int8)

    c_offset = reader.read(Types.uint32)
    c_reader = reader.jump_to(c_offset)
    b6 = read_c(c_reader)

    b7_size = reader.read(Types.uint32)
    b7_offset = reader.read(Types.uint32)
    b7_reader = reader.jump_to(b7_offset)
    b7 = [read_d(reader.jump_to(b7_reader.read(Types.uint32)))
          for _ in range(b7_size)]

    b8 = reader.read(Types.uint32)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8)


def read_a(reader):
    a1 = reader.read(Types.int8)
    a2 = read_b(reader)
    a3 = reader.read(Types.int32)
    a4 = [reader.read(Types.int16) for _ in range(4)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4)


def main(data):
    return read_a(BinaryReader(data, 5))


print(main(b'ABMA\xd21\xd3#~[\xbf\xd5\x82\xfa[\x04\x002\x00\x00\x00\xcd6\x00'
           b'\x00\x00\x02\x00\x00\x00|\x00\x00\x00\x9a)\xbb\x1af\xcd,\xcb\x9c\xad\x90=6#'
           b'F$yfve\xd8\xd4m[9y$\x9d\xa2>\xd1\xf9J?\xba\xdb\t?SwB\xbfwPn\xbf\xdcr">'
           b'2Z\x04\xbf\xe2\xd8\xdf>\xb1R@?Y\xaf\x18?\x9f\x0c6?B\xa31?*\x1fc\xbf'
           b'\x82\x19\xf7>\x17A\xff\xbe\x8d@s\xbd<\x00\x00\x00\\\x00\x00\x00'))
