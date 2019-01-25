import numpy as np
import sys
sys.path.append('../example/')
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)
    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))
    # generate a new random vector of length 10
    x = np.random.rand(10)
    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))


odd = np.array([1,2,4,0,1])
even=np.array([1,6,5,4])
test2=np.random.randint(low=-10, high=500,size=100)
blank=np.array([])
single=np.array([1])
duplicate=np.array([1,1,1])
duplicate2=np.array([1,50,50,3,4,1,6,50])
def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    algs.bubblesort(odd)
    algs.bubblesort(even)
    algs.bubblesort(test2)
    algs.bubblesort(blank)
    algs.bubblesort(single)
    algs.bubblesort(duplicate)
    algs.bubblesort(duplicate2)




#print('Quicksort:')
#print(quicksort(test1))
def test_quicksort():
    # for now, just attempt to call the quicksort function, should
    # actually check output
    algs.quicksort(odd)
    algs.quicksort(even)
    algs.quicksort(test2)
    algs.quicksort(blank)
    algs.quicksort(single)
    algs.quicksort(duplicate)
    algs.quicksort(duplicate2)

print('Testing Bubblesort.')
test_bubblesort()
print('Testing Quicksort.')
test_quicksort()
