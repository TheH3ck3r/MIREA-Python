class HashTable:
    def __init__(self):
        self.table = []

    def __setitem__(self, key, value):
        hashed_key = hash(key)
        for i, (k) in enumerate(self.table):
            if k == hashed_key:
                self.table[i] = (hashed_key, value)
                return
        self.table.append((hashed_key, value))

    def __getitem__(self, key):
        hashed_key = hash(key)
        for k, v in self.table:
            if k == hashed_key:
                return v
        raise KeyError(key)

    def __len__(self):
        return len(self.table)


def main():
    # Пример использования
    ht = HashTable()
    ht['key1'] = 'value1'
    ht['key2'] = 'value2'
    ht['key2'] = 'value3'

    print(ht['key1'])  # Выведет 'value1'
    print(ht['key2'])  # Выведет 'value2'
    print(len(ht))     # Выведет 3


if __name__ == '__main__':
    main()