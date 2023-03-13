from random import randint
'''归并排序'''


def merge(items1, items2, comp=lambda x, y: x < y):
    items = []
    i, j = 0, 0
    while i < len(items1) and j < len(items2):
        if comp(items1[i], items2[j]):
            items.append(items1[i])
            i += 1
        else:
            items.append(items2[j])
            j += 1
    items += items1[i:]
    items += items2[j:]
    return items


def merge_sort(items, comp=lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    if len(items) < 2:
        return items
    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def main():
    items = [randint(1, 100) for _ in range(10)]
    print(merge_sort(items))


if __name__ == '__main__':
    main()
