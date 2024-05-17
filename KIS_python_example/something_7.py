
def main(x: list):
    some = {
        "JFLEX": {
            2020: {
                "GOSU": 0,
                "PIC": {
                    2005: 1,
                    1957: 2
                },
                "RAGEL": 3
            },
            2008: {
                "GOSU": {
                    2005: 4,
                    1957: 5
                },
                "PIC": {
                    "MASK": 6,
                    "RAML": 7,
                    "PERL6": 8
                },
                "RAGEL": {
                    "MASK": 9,
                    "RAML": 10,
                    "PERL6": 11
                }
            }
        },
        "DART": 12,
    }
    if x[4] == "DART":
        return 12
    else:
        if x[1] == 2020:
            if x[2] != "PIC":
                return some[x[4]][x[1]][x[2]]
            else:
                return some[x[4]][x[1]][x[2]][x[3]]
        else:
            if x[2] != "GOSU":
                return some[x[4]][x[1]][x[2]][x[0]]
            else:
                return some[x[4]][x[1]][x[2]][x[3]]


if __name__ == '__main__':
    print(main(['RAML', 2008, 'RAGEL', 1957, 'DART']))
    print(main(['RAML', 2008, 'RAGEL', 2005, 'JFLEX']))
    print(main(['RAML', 2020, 'PIC', 1957, 'JFLEX']))
    print(main(['MASK', 2008, 'PIC', 2005, 'JFLEX']))
    print(main(['MASK', 2008, 'RAGEL', 1957, 'JFLEX']))
