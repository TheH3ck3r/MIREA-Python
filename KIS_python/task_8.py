import re


def main(s: str):
    result = []
    pattern_1 = r"var\s*{([\d\s\.\#\-]*)}\s*=:\s*(.+?)\s*</sect>"
    pattern_2 = r"#(-?\w+)"
    matches_1 = re.findall(pattern_1, s)
    for match_1 in matches_1:
        matches_2 = re.findall(pattern_2, match_1[0])
        new_tuple = (
            match_1[len(match_1) - 1],
            [int(match) for match in matches_2],
        )
        result.append(new_tuple)
    return result

input_str = "<sect> <sect> var{ #-2625 .#2821 . #955 .#4021 } =: eroror_853</sect><sect> var { #8115 . #7851 . #-6382 } =: ribera </sect><sect> var{ #-5874 . #2135 } =: usbeen_689 </sect> <sect> var{#-6227 . #5446} =: rabidi </sect> </sect>"

if __name__ == '__main__':
    print(main(input_str))