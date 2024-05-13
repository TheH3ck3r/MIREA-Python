
def find_word(string: str, word: str):
    """
    >>> find_word('Какой-то текст', 'Какой')
    [0]
    >>> find_word('Какой-то текст', 'Никакой')
    [-1]
    """
    checker = True
    massive = []
    from_index = 0
    try:
        while checker:
            from_index = string.index(word, from_index)
            massive.append(from_index)
            from_index = from_index + 1
            if from_index >= len(string)-1:
                checker = False
    except Exception:
        if massive == []:
            massive = [-1]
        else:
            pass
    finally:
        return massive


if __name__ == "__main__":
    print(find_word(string="some website", word="smue"))
