def insertion_sort(iterable, order=True):

    for i in range(1, len(iterable)):
        j=i
        while j > 0 and iterable[j] < iterable[j-1] and order:
            iterable[j], iterable[j-1] = iterable[j-1], iterable[j]
            j-=1
        while j > 0 and not (iterable[j] < iterable[j-1] or order) :
            iterable[j], iterable[j-1] = iterable[j-1], iterable[j]
            j-=1
    return iterable

def insertion_sort_recursive(iterable, order=True, i=0, j=1):

    if len(iterable) <= 1:
        return iterable

    if j == len(iterable) :
        return iterable

    if j == 0 :
        return insertion_sort_recursive(iterable, order, i+1, i+2)

    if iterable[j] < iterable[j-1] and order:
        iterable[j], iterable[j-1] = iterable[j-1], iterable[j]
        return insertion_sort_recursive(iterable, order, i, j - 1)
    if not (iterable[j] < iterable[j-1] or order):
        iterable[j], iterable[j-1] = iterable[j-1], iterable[j]
        return insertion_sort_recursive(iterable, order, i, j - 1)

    return insertion_sort_recursive(iterable, order, i+1, i+2)

def test_insertion_sort():

    assert insertion_sort([-3, 2, 1, 5, 4, 3, -1, 0, 2]) == [-3, -1, 0, 1, 2, 2, 3, 4, 5]
    assert insertion_sort(['a', 'c', 'd', 'b', 'e', 'a'], False) == ['e', 'd', 'c', 'b', 'a', 'a']
    print("All tests passed for insertion_sort function!")

def test_insertion_sort_recursive():
    assert insertion_sort_recursive([2, 1, 5, 4, 3, -1, 0, 2]) == [-1, 0, 1, 2, 2, 3, 4, 5]
    assert insertion_sort_recursive([4, -23, 7, 82, 91, 8, 1, 1, -4]) == [-23, -4, 1, 1, 4, 7, 8, 82, 91]
    assert insertion_sort_recursive(['a', 'c', 'd', 'b', 'e', 'a'], False) == ['e', 'd', 'c', 'b', 'a', 'a']
    print("All tests passed for insertion_sort_recursive function!")

test_insertion_sort()
test_insertion_sort_recursive()
