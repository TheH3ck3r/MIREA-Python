def main(x: list):
    some = {
        "XOJO": {
            "SAS": {
                1978: 0,
                2020: 1,
                1971: 2
            },
            "JSON5": 3
        },
        "RDOC": {
            1978: 4,
            2020: 5,
            1971: {
                "GOLO": 6,
                "XPROC": 7
            }
        },
        "NINJA": {
            "SAS": 8,
            "JSON5": 9
        }
    }
    if x[0] == "XOJO" and x[2] == "JSON5":
        return 3
    elif x[0] == "RDOC":
        if x[1] == 1978:
            return 4
        elif x[1] == 2020:
            return 5
        else:
            return some[x[0]][x[1]][x[3]]
    elif x[0] == "NINJA":
        return some[x[0]][x[2]]
    else:
        return some[x[0]][x[2]][x[1]]



if __name__ == '__main__':
    print(main(['NINJA', 1971, 'SAS', 'GOLO']))   
    print(main(['XOJO', 1978, 'SAS', 'GOLO']))  
    print(main(['XOJO', 1971, 'JSON5', 'XPROC']))
    print(main(['RDOC', 2020, 'JSON5', 'XPROC']))
    print(main(['XOJO', 2020, 'SAS', 'XPROC']))