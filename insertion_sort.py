"""
Recursive insertion sort implementation in Python 3
https://en.wikipedia.org/wiki/Insertion_sort
"""
def insert(x, lis):
    """
    Insert element at the right position in the list.
    :param lis:    list
    :param element: element to be inserted
    """
    if lis == list():
        return [x]
    elif lis[0] >= x:
        return [x] + lis
    else:
        return [lis[0]] + insert(x,lis[1:])

def insertion_sort(lis):
    """
    Implementation of recursive insertion sort.
    :param lis: list to be sorted
    """
    if lis == list():
        return list()
    else:
        return insert(lis[0], insertion_sort(lis[1:]))

def main():
    lis1 = [4, 1, 2, 3, 9]
    lis2 = [1]
    lis3 = [2, 2, 1, -1, 0, 4, 5, 2]

    lis1 = insertion_sort(lis1)
    assert lis1 == [1, 2, 3, 4, 9]

    lis2 = insertion_sort(lis2)
    assert lis2 == [1]

    lis3 = insertion_sort(lis3)
    assert lis3 == [-1, 0, 1, 2, 2, 2, 4, 5]

if __name__ == '__main__':
    main()
            