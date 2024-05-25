import re


def main(s):
    pattern = r'\\begin glob (\w+)\s*<==\s*#\s*(-?\d+)\.\s*\\end'
    matches = re.findall(pattern, s)
    result = {key: int(value) for key, value in matches}
    return result


input_string = "<% \\begin glob lece_974<== #2533. \\end, \\begin glob beisbi <== #-2301. \\end, %>"
print(main(input_string))
