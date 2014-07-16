"""     @author:        Guang Yang
        @mktime:        7/15/2014
        @description:   Demo on %time in IPython: insertion sort vs merge sort
"""

# -- Timing Code without IPython --
def dumb_timer(i_fun, i_list, iter_num=1):
    """
    An ad-hoc implementation of a timer to count the speed of the two sort functions

    Args: 
    i_fun (method):     the sorting method
    i_list (list):      the input unsorted list
    iter_num:           the number of iterations desired

    Return:
    elapsed_per(float): the average time spent to run the function
    """

    import time
    start = time.time()
    for i in range(iter_num):
        i_fun(i_list[:])
    elapsed_per = (time.time() - start) / iter_num
    return elapsed_per





def insertion_sort(i_list):
    """
    Implementing the insertion sort in ascension using swaps
    
    Args:
    i_list (list): (unsorted) list of integers

    Return:
    None: the input list will be sorted as a result

    Example:
    >>> insertion_sort([1, 5, 2, 3, 10, 0])
    [0, 1, 2, 3, 5, 10]
    """

    for i in xrange(1,len(i_list)):
        current_val = i_list[i]
        j = i - 1   #index for the left of current value
        while (j >= 0) and (i_list[j] > current_val):
            i_list[j+1] = i_list[j]
            j = j - 1
        i_list[j+1] = current_val
    

def merge_sort(i_list):
    """
    Implementing the merge sort in ascension using bisection

    Args:
    i_list (list): (unsorted) list of integers

    Return:
    None: the input list will be sorted as a result

    Example:
    >>> merge_sort([1, 5, 2, 3, 4, 20]
    [1, 2, 3, 4, 5, 20]
    """

    _mergesort(i_list, 0, len(i_list) - 1)

def _mergesort(i_list, first, last):
    # break problem into smaller structurally identical pieces
    mid = (first + last) / 2
    if first < last:
        _mergesort( i_list, first, mid )
        _mergesort( i_list, mid + 1, last )
   
    # merge solved pieces to get solution to original problem
    a, f, l = 0, first, mid + 1
    tmp = [None] * (last - first + 1)
   
    while f <= mid and l <= last:
        if i_list[f] < i_list[l] :
            tmp[a] = i_list[f]
            f += 1
        else:
            tmp[a] = i_list[l]
            l += 1
        a += 1
   
    if f <= mid :
        tmp[a:] = i_list[f:mid + 1]
   
    if l <= last:
        tmp[a:] = i_list[l:last + 1]
   
    a = 0
    while first <= last:
        i_list[first] = tmp[a]
        first += 1
        a += 1
