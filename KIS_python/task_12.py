from struct import unpack_from, calcsize


class Types:
    double = 'd'
    int32 = 'i'
    int16 = 'h'
    uint16 = 'H'
    uint8 = 'B'
    int8 = 'b'
    int64 = 'q'
    uint32 = 'I'
    char = 's' # или 'c'
    uint64 = 'Q'
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
    f1 = reader.read(Types.int16)

    f2 = [reader.read(Types.int8) for _ in range(6)]

    f3_size = reader.read(Types.uint32)
    f3_offset = reader.read(Types.uint32)
    f3_reader = reader.jump_to(f3_offset)
    f3 = [f3_reader.read(Types.uint8) for _ in range(f3_size)]

    f4 = reader.read(Types.uint32)
    return dict(F1=f1, F2=f2, F3=f3, F4=f4)


def read_e(reader):
    e1 = reader.read(Types.uint64)
    e2 = reader.read(Types.double)
    e3 = reader.read(Types.uint8)
    return dict(E1=e1, E2=e2, E3=e3)


def read_d(reader):
    d1 = read_e(reader)
    d2 = reader.read(Types.uint64)
    return dict(D1=d1, D2=d2)


def read_c(reader):
    c1 = reader.read(Types.int8)
    c2 = reader.read(Types.float)
    c3 = reader.read(Types.int32)
    c4 = [reader.read(Types.uint8) for _ in range(4)]
    return dict(C1=c1, C2=c2, C3=c3, C4=c4)


def read_b(reader):
    b1 = reader.read(Types.int64)
    b2 = reader.read(Types.uint64)

    b3_size = reader.read(Types.uint32)
    b3_offset = reader.read(Types.uint32)
    b3_reader = reader.jump_to(b3_offset)
    b3 = [read_c(reader.jump_to(b3_reader.read(Types.uint32)))
          for _ in range(b3_size)]

    b4 = reader.read(Types.int32)
    b5 = reader.read(Types.uint32)
    b6 = reader.read(Types.int16)
    b7 = reader.read(Types.uint32)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7)


def read_a(reader):
    a1 = reader.read(Types.int32)
    a2 = reader.read(Types.uint32)

    b_offset = reader.read(Types.uint32)
    b_reader = reader.jump_to(b_offset)
    a3 = read_b(b_reader)

    d_offset = reader.read(Types.uint32)
    d_reader = reader.jump_to(d_offset)
    a4 = read_d(d_reader)

    a5 = reader.read(Types.uint64)

    f_offset = reader.read(Types.uint32)
    f_reader = reader.jump_to(f_offset)
    a6 = read_f(f_reader)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)


def main(data):
    return read_a(BinaryReader(data, 3))


print(main(b"UZH\x80\xd7\xa1\x91\xe3\x1fK\x00\x00\x00e\x00\x08O'\xee\xf4\x88\xe1"
           b'&\x81\x00\x00\x00xZ\xb8v?\xee<\xa2\x8eY\xfd\x84\xef\x03k\xca\xb3>t\xf0=]v'
           b'r\x99\xa1\x1d\x00\x00\x00*\x00\x00\x00\xf9*#Z\xdd\x81\xbdiO\x07K\x9c^'
           b'\xb9\xdeO\x02\x00\x00\x007\x00\x00\x00J\xa6\x85\x92,G\x01h\xb7\xddxr)'
           b'\xea\x92"\xb2\x08\xc9\xea7J\xcc9\xe5\xb9>\x0f\xe4\xbf\xf8\xb5\xf5'
           b'\x1d\xaa`\x15\x9d;\x06(\x1d\x8b\x98\t\xde\x97\xbd\xe0\xf5\x03\x00\x00'
           b'\x00~\x00\x00\x009\x8f\x9a\x9e'))