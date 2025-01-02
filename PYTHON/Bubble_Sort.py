def bubble_sort(iterable,order=True):

    #This function returns a sorted list of numbers and strings (iterable) in ascending (order=True) and descending (order=False) order
    #by using the well-known bubble_sort algorithm.

    #Time Complexity: O(n^2)

    
    for i in range(0,len(iterable)):
        for j in range(i+1,len(iterable)) :
            if iterable[i]>iterable[j] and order :
                iterable[i],iterable[j]=iterable[j],iterable[i]
            elif not(iterable[i]>iterable[j] or order) :
                iterable[i],iterable[j]=iterable[j],iterable[i]
                
    return iterable
                
def test_bubble_sort():

    #This function tests the bubble_sort algorithm written within the bubble_sort function.

    assert bubble_sort([2,1,5,4,3,-1,0,2]) == [-1,0,1,2,2,3,4,5]
    assert bubble_sort(['a','c','d','b','e','a'])  == ['a','a','b','c','d','e']
    print("All tests passed!")

   
def main():
    test_bubble_sort()
                
main()
                
 
