import re


def main(s):
    pattern = r'<data>\s*declare\s*#(-?\d+)\s*to\s*`(\w+)\.\s*</data>'
    matches = re.findall(pattern, s)
    result = {name: int(number) for number, name in matches}
    return result


input_string = "((<data> declare #2441 to `rein. </data>, <data> declare#2120 to `esaesle. </data>, ))"
print(main(input_string))
