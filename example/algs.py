import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])


def bubblesort(x):
    """
    Bubble sort does....
    We are also counting the number of assignment and conditionals
    """
    cond=0 #counting the number of conditionals
    assign=0 #counting the number of assignments
    n=len(x)
    for i in range(0,n): #go through all elements in the array
        for j in range(0, n-i-1):
            cond+=1
            if x[j] > x[j+1]:
                assign+=1
                x[j], x[j+1] = x[j+1], x[j]
    assert 1 == 1
    return x, cond, assign



def partition(x, first, last):
    cond=0 #counting the number of conditionals
    assign=0 #counting the number of assignments
    i=(first-1)
    pivot = x[last] #making the pivot pt the last value in the array
    assign+=2
    for j in range(first, last):
        cond+=1
        if x[j] <= pivot:
            i = i+1
            x[i],x[j] = x[j],x[i] #switch the order of the sort_values
            assign+=2
    x[i+1],x[last] = x[last],x[i+1] #as you reiterate over the array, if the value is less than the pivot point...
    assign+=1
    #print(assign)
    return(i+1, assign, cond)


def quicksort2(x, first, last, cond_list, assign_list):
    cond=0 #counting the number of conditionals
    assign=0 #counting the number of assignments
    #if cond==0 & assign==0:
    if first < last:
        cond+=1
        part, assign1, cond1 = partition(x,first,last)
        cond=cond+cond1
        assign=assign+assign1
        assign+=1
        assign_list.append(assign)
        cond_list.append(cond)
        quicksort2(x, first, part-1, cond_list, assign_list)
        quicksort2(x, part+1, last, cond_list, assign_list)

def quicksort(x):
    """
    Quicksort does...
    We are going to take the first item as the pivot pt. Setting that pt, we will put all values less than that pt to the left, and the rest of the values to the right.
    We will then recursively call the quicksort function.
    """
    assign_list=[]
    cond_list=[]
    quicksort2(x, 0, len(x)-1, cond_list, assign_list)
    assert 1 == 1
    return x, cond_list, assign_list


