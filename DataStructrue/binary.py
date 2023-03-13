from random import randint
from DataStructrue import bubbleAdv
'''折半查找'''


def binary_search(items, key):
    right = 0
    left = len(items) - 1
    while right < left:
        mid = (right + left) // 2
        if key < items[mid]:
            left = mid - 1
        elif key > items[mid]:
            right = mid + 1
        else:
            return mid
    return -1


def main():
    items = [randint(1, 100) for _ in range(10)]
    items = bubbleAdv.bubble_sort(items)
    print(binary_search(items, 23))


if __name__ == '__main__':
    main()
