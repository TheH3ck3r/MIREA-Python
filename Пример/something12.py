from struct import unpack_from, calcsize


class Types:
    float = 'f'
    char = 's'  # или 'c'
    int8 = 'b'
    uint16 = 'H'
    uint32 = 'I'
    uint8 = 'B'
    int16 = 'h'
    int32 = 'i'
    uint64 = 'Q'
    int64 = 'q'
    double = 'd'


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
    e2 = reader.read(Types.int16)
    e3 = reader.read(Types.int16)

    return dict(E1=e1, E2=e2, E3=e3)


def read_d(reader):
    d1 = reader.read(Types.uint8)
    d2 = reader.read(Types.int64)
    d3 = reader.read(Types.int32)
    d4 = reader.read(Types.uint32)
    d5 = reader.read(Types.uint64)
    d6 = reader.read(Types.float)

    return dict(D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6)


def read_c(reader):
    c1 = reader.read(Types.int32)
    c2 = reader.read(Types.int32)

    c3_size = reader.read(Types.uint32)
    c3_offset = reader.read(Types.uint32)
    c3_reader = reader.jump_to(c3_offset)
    c3 = b''.join([c3_reader.read(Types.char)
                   for _ in range(c3_size)]).decode()

    c4 = reader.read(Types.float)
    c5 = reader.read(Types.int8)
    c6 = reader.read(Types.double)
    c7 = reader.read(Types.uint64)

    c8 = [reader.read(Types.uint16) for _ in range(2)]
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5, C6=c6, C7=c7, C8=c8)


def read_b(reader):
    c_offset = reader.read(Types.uint32)
    c_reader = reader.jump_to(c_offset)
    b1 = read_c(c_reader)

    d_offset = reader.read(Types.uint32)
    d_reader = reader.jump_to(d_offset)
    b2 = read_d(d_reader)

    return dict(B1=b1, B2=b2)


def read_a(reader):
    a1 = reader.read(Types.uint32)

    b_offset = reader.read(Types.uint32)
    b_reader = reader.jump_to(b_offset)
    a2 = read_b(b_reader)

    a3 = reader.read(Types.uint16)

    a4_size = reader.read(Types.uint32)
    a4_offset = reader.read(Types.uint16)
    a4_reader = reader.jump_to(a4_offset)
    a4 = [read_e(reader.jump_to(a4_reader.read(Types.uint16)))
          for _ in range(a4_size)]

    a5_size = reader.read(Types.uint16)
    a5_offset = reader.read(Types.uint32)
    a5_reader = reader.jump_to(a5_offset)
    a5 = [a5_reader.read(Types.int32) for _ in range(a5_size)]

    a6 = reader.read(Types.uint16)
    a7 = [reader.read(Types.uint16) for _ in range(5)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7)


def main(data):
    return read_a(BinaryReader(data, 4))


print(main(b'USFP\x9c.q\xa5n\x00\x00\x00|\xb9\x03\x00\x00\x00\x85\x00\x02\x00\x8b\x00'
           b'\x00\x00{\x145\x1f\x8ck\x05\xe0\xca\xa3\x13\xfdxm"T\xae\xe5\x98r>P'
           b'\x02\x00\x00\x00&\x00\x00\x001\xf1\x1a\xbcp\x90\x1f\xad \xda\xc8\xd5?RV\x8a'
           b"\x10F,fHk\x11\xa9'j$\x05\x9a&\x1b\xfc\xbb\xf5o\xad\x0bE_\xf83|\xb1\xb0"
           b'\xdc\xd5h\x1a\n\x1a\xda&\xed\xbe(\x00\x00\x00Q\x00\x00\x00\xb4\xb3'
           b'^\xe5\xac\x12\x82\xf1N\x0b\x0fn*&#v\x00{\x00\x80\x00\x9dG\x1e\xaf\xb8'
           b'+\xa4\x1b'))
