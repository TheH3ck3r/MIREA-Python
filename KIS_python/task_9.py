import re


def main(input_str):
    pattern = (
        r"var\s*\{\s*"
        r"#(-?\d+)\s*\.\s*"
        r"#(-?\d+)\s*"
        r"(?:\.\s*#(-?\d+)\s*)*"
        r"\}\s*=\s*:\s*"
        r"([\w_]+)\s*"
        r"</sect>"
    )
    matches = re.findall(pattern, input_str)
    result = []
    for match in matches:
        nums = [int(num) for num in match[:-1] if num]
        name = match[-1]
        result.append((name, nums))
    return result

input_str = "<sect> <sect> var{ #-2625 .#2821 . #955 .#4021 } =: eroror_853</sect><sect> var { #8115 . #7851 . #-6382 } =: ribera </sect><sect> var{ #-5874 . #2135 } =: usbeen_689 </sect> <sect> var{#-6227 . #5446} =: rabidi </sect> </sect>"

if __name__ == '__main__':
    print(main(input_str))