def partition(iterable, left, right, order):

    pivot = iterable[right]
    i = left -1
    j = left
    while j < right:
        if iterable[j] <= pivot and order or not (iterable[j] <= pivot or order) :
            i += 1
            iterable[i], iterable[j] = iterable[j], iterable[i]
            j += 1
        else :
            j+=1
    iterable[i+1], iterable[j] = iterable[j], iterable[i+1]
    return i+1
  
def quick_sort_algorithm(iterable, left, right, order=True):

    if left < right :
        index_cut = partition(iterable, left, right, order)
        quick_sort_algorithm(iterable, left, index_cut-1, order)
        quick_sort_algorithm(iterable, index_cut+1, right, order)

    return iterable
  
def quick_sort(iterable, order=True):
  
    return quick_sort_algorithm(iterable, 0, len(iterable)-1, order)

def test_quick_sort():
  
    assert quick_sort([2, 1, 5, 4, 3, -1, 0, 2]) == [-1, 0, 1, 2, 2, 3, 4, 5]
    assert quick_sort([4, -23, 7, 82, 91, 8, 1, 1, -4]) == [-23, -4, 1, 1, 4, 7, 8, 82, 91]
    assert quick_sort(['a', 'c', 'd', 'b', 'e', 'a'], False) == ['e', 'd', 'c', 'b', 'a', 'a']
    print("All tests passed for quick_sort function!")

test_quick_sort()
