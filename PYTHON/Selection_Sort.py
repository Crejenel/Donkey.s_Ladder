def selection_sort(iterable, order=True):

    for i in range(0, len(iterable)):
        poz = i
        for j in range(i + 1, len(iterable)):
            if iterable[poz] > iterable[j] and order:
                poz = j
            elif not (iterable[poz] > iterable[j] or order):
                poz = j
        iterable[i], iterable[poz] = iterable[poz], iterable[i]

    return iterable

def selection_sort_recursive(iterable, order=True, i=0, j=1, poz=0):

    if len(iterable) <= 1:
        return iterable

    if i == len(iterable) - 1 :
        return iterable

    if iterable[poz] > iterable[j] and order:
        poz = j
    elif not (iterable[poz] > iterable[j] or order):
        poz = j
    if j != len(iterable)-1:
        return selection_sort_recursive(iterable, order, i, j+1, poz)
    else :
        iterable[poz], iterable[i] = iterable[i], iterable[poz]
        return selection_sort_recursive(iterable, order, i+1, i+2, poz=i+1)

def test_selection_sort():

    assert selection_sort([-3, 2, 1, 5, 4, 3, -1, 0, 2]) == [-3, -1, 0, 1, 2, 2, 3, 4, 5]
    assert selection_sort(['a', 'c', 'd', 'b', 'e', 'a'],False) == ['e','d','c','b','a','a']
    print("All tests passed for selection_sort function!")

def test_selection_sort_recursive():

    assert selection_sort_recursive([2, 1, 5, 4, 3, -1, 0, 2]) == [-1, 0, 1, 2, 2, 3, 4, 5]
    assert  selection_sort_recursive([4, -23, 7, 82, 91, 8, 1, 1, -4]) == [-23, -4, 1, 1, 4, 7, 8, 82, 91]
    assert selection_sort_recursive(['a', 'c', 'd', 'b', 'e', 'a'],False) == ['e','d','c','b','a','a']
    print("All tests passed for selection_sort_recursive function!")

test_selection_sort()
test_selection_sort_recursive()
