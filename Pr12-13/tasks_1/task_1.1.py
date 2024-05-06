
def find_word(string: str, word: str):
    """
    >>> find_word('Какой-то текст', 'Какой')
    0
    >>> find_word('Какой-то текст', 'Никакой')
    -1
    """
    try:
        result = string.index(word)
    except Exception:
        result = -1
    finally:
        return result


if __name__ == "__main__":
    print(find_word(string="gay website", word="gey"))