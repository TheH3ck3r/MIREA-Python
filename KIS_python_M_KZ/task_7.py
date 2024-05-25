def main(x: list):
    some = {
        "BISON": {
            1969: {
                2009: 0,
                2007: 1,
                1965: 2
            },
            2016: {
                2015: 3,
                1991: {
                    2009: 4,
                    2007: 5,
                    1965: 6
                },
                1996: {
                    1973: 7,
                    1969: 8,
                    1989: 9
                }
            }
        },
        "IO": 10,
        "NIM": 11
    }
    
    if x[3] == "BISON":
        if x[1] == 1969:
            return some[x[3]][x[1]][x[2]]
        else:
            if x[4] == 2015:
                return 3
            elif x[4] == 1991:
                return some[x[3]][x[1]][x[4]][x[2]]
            elif x[4] == 1996:
                return some[x[3]][x[1]][x[4]][x[0]]
    elif x[3] == "IO":
        return 10
    elif x[3] == "NIM":
        return 11
    return None


if __name__ == '__main__':
    print(main([1973, 2016, 2007, 'NIM', 1991]))  # = 11
    print(main([1973, 2016, 2007, 'BISON', 1996]))  # = 7
    print(main([1989, 2016, 2007, 'BISON', 2015]))  # = 3
    print(main([1969, 1969, 1965, 'IO', 1991]))  # = 10
    print(main([1989, 1969, 1965, 'BISON', 2015]))  # = 2
