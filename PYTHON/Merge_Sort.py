def merge_sort_algorithm(iterable, left, right, order=True):

    if left < right:
        middle = (left + right) // 2
        merge_sort_algorithm(iterable, left, middle, order)
        merge_sort_algorithm(iterable, middle+1, right, order)
        c=[]
        index_left = left
        index_right = middle + 1
        while index_left <= middle and index_right <= right:
            if (iterable[index_left] < iterable[index_right] and order) or not(iterable[index_left] < iterable[index_right] or order):
                c.append(iterable[index_left])
                index_left += 1
            else :
                c.append(iterable[index_right])
                index_right += 1
        while index_left <= middle:
            c.append(iterable[index_left])
            index_left += 1
        while index_right <= right:
            c.append(iterable[index_right])
            index_right += 1
        iterable[left:right+1] = c

    return iterable
  
def merge_sort(iterable, order=True):
  
    return merge_sort_algorithm(iterable, 0, len(iterable)-1, order)


def test_merge_sort():
  
    assert merge_sort([2, 1, 5, 4, 3, -1, 0, 2]) == [-1, 0, 1, 2, 2, 3, 4, 5]
    assert merge_sort([4, -23, 7, 82, 91, 8, 1, 1, -4]) == [-23, -4, 1, 1, 4, 7, 8, 82, 91]
    assert merge_sort(['a', 'c', 'd', 'b', 'e', 'a'], False) == ['e', 'd', 'c', 'b', 'a', 'a']
    print("All tests passed for merge_sort function!")

test_merge_sort()
