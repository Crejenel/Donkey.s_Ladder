def bubble_sort(iterable, order=True, issorted=True):

    inplace=0
    while issorted:
        i = 0
        for j in range(i+1, len(iterable)-inplace):
            if iterable[i] > iterable[j] and order:
                iterable[i], iterable[j] = iterable[j], iterable[i]
                issorted=False
            elif not (iterable[i] > iterable[j] or order):
                iterable[i], iterable[j] = iterable[j], iterable[i]
                issorted=False
            i+=1
        if issorted:
            return iterable
        else :
            inplace+=1
            issorted=True


def bubble_sort_recursive(iterable, order=True, issorted=True, inplace=0, i=0, j=1):

    if len(iterable) <= 1:
        return iterable

    if j==len(iterable)-inplace:
        if issorted:
            return iterable
        else :
            return bubble_sort_recursive(iterable, order, True, inplace+1, 0, 1)

    if iterable[i] > iterable[j] and order:
        iterable[i], iterable[j] = iterable[j], iterable[i]
        return bubble_sort_recursive(iterable, order, False, inplace, i+1, j+1)
    elif not (iterable[i] > iterable[j] or order):
        iterable[i], iterable[j] = iterable[j], iterable[i]
        return bubble_sort_recursive(iterable, order, False, inplace, i+1, j+1)
    else :
        return bubble_sort_recursive(iterable, order, issorted, inplace, i+1, j+1)


def test_bubble_sort():

    assert bubble_sort([-3, 2, 1, 5, 4, 3, -1, 0, 2]) == [-3, -1, 0, 1, 2, 2, 3, 4, 5]
    assert bubble_sort(['a', 'c', 'd', 'b', 'e', 'a'], False) == ['e', 'd', 'c', 'b', 'a', 'a']
    print("All tests passed for bubble_sort function!")


def test_bubble_sort_recursive():

    assert bubble_sort_recursive([2, 1, 5, 4, 3, -1, 0, 2]) == [-1, 0, 1, 2, 2, 3, 4, 5]
    assert bubble_sort_recursive([4, -23, 7, 82, 91, 8, 1, 1, -4]) == [-23, -4, 1, 1, 4, 7, 8, 82, 91]
    assert bubble_sort_recursive(['a', 'c', 'd', 'b', 'e', 'a'], False) == ['e', 'd', 'c', 'b', 'a', 'a']
    print("All tests passed for bubble_sort_recursive function!")

test_bubble_sort()
test_bubble_sort_recursive()
