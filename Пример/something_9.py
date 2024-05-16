import re


def main(s: str):
    result = {}
    pattern = r"store\s?q\((\w+)\)\s?=>\s?'(\w+)';"
    matches = re.findall(pattern, s)
    for match in matches:
        result[match[1]] = match[0]
    return result


if __name__ == '__main__':
    print(main("<< || store q(edusxe)=>'zaes'; ||, || store q(aqu_432)=> 'edlebi';||, || store q(bitied_924) =>'veesso_766'; >>"))
