from random import randint
'''快速排序'''


def quick_sort(items, comp=lambda x, y: x <= y):
    items = items[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, right, left, comp):
    if right < left:
        pos = partition(items, right, left, comp)
        _quick_sort(items, right, pos - 1, comp)
        _quick_sort(items, pos + 1, left, comp)


def partition(items, right, left, comp):
    pivot = items[right]
    while right < left:
        while right < left and comp(pivot, items[left]):
            left -= 1
        items[right] = items[left]
        while right < left and comp(items[right], pivot):
            right += 1
        items[left] = items[right]
    items[right] = pivot
    return right


def main():
    items = [randint(1, 100) for _ in range(10)]
    print(quick_sort(items))


if __name__ == '__main__':
    main()
