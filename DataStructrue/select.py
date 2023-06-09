def select_sort(items, comp=lambda x, y: x < y):
    '''简单选择排序'''
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                items[j], items[min_index] = items[min_index], items[j]
    return items


def main():
    items = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(select_sort(items))


if __name__ == '__main__':
    main()
