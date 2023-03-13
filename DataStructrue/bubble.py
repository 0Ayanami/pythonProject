def bubble_sort(items, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break
    return items


def main():
    items = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(bubble_sort(items))


if __name__ == '__main__':
    main()
