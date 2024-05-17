def main(x: list):
    some = {
        1977: {
            1962: {
                "YACC": {
                    "C": 0,
                    "APL": 1
                },
                "CUDA": {
                    "C": 2,
                    "APL": 3
                },
                "JFLEX": 4
            },
            2013: 5
        },
        2016: {
            "C": {
                "ROFF": {
                    1962: 6,
                    2013: 7
                },
                "NGINX": 8,
                "APL": {
                    "YACC": 9,
                    "CUDA": 10,
                    "JFLEX": 11
                }
            },
            "APL": 12
        }
    }
    if (x[0] == 1977):
        if (x[3] == "JFLEX"):
            return 4
        elif (x[0] == 1977 and x[4] == 2013):
            return 5
        else:
            return some[x[0]][x[4]][x[3]][x[2]]
    elif(x[0] == 2016):
        if (x[2] == "APL"):
            return 12
        elif (x[2] == "C" and x[1] == "NGINX"):
            return 8
        elif (x[1] == "ALP"):
            return some[x[0]][x[2]][x[1]][x[3]]
        elif (x[1] == "ROFF"):
            return some[x[0]][x[2]][x[1]][x[4]]


if __name__ == '__main__':
    print(main([2016, 'APL', 'C', 'CUDA', 2013]))   
    print(main([1977, 'NGINX', 'APL', 'YACC', 2013]))  
    print(main([2016, 'ROFF', 'C', 'CUDA', 1962]))
    print(main([2016, 'NGINX', 'C', 'YACC', 2013]))
    print(main([2016, 'NGINX', 'APL', 'JFLEX', 1962]))