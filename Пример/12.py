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
