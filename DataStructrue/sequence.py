from random import randint


def sequence_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def main():
    items = [randint(1, 100) for _ in range(10)]
    print(sequence_search(items, 9))


if __name__ == '__main__':
    main()
