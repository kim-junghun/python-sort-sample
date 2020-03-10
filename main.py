import copy
import random
import sys
import timeit

from sort import *


def make_sample_list(high):
    sample = list(range(1, high + 1))
    random.shuffle(sample)
    return sample


if __name__ == '__main__':    
    length = 100
    origin = make_sample_list(length)
    print(origin)
    # ---------------------------------------
    # bubble sort
    sample = copy.deepcopy(origin)
    print('bubble')    
    start = timeit.default_timer()
    bubble.sort(sample)
    stop = timeit.default_timer()    
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # selection sort
    sample = copy.deepcopy(origin)
    print('selection')    
    start = timeit.default_timer()
    selection.sort(sample)
    stop = timeit.default_timer()    
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # quick sort
    sample = copy.deepcopy(origin)
    print('quick')    
    start = timeit.default_timer()
    quick.sort(sample)
    stop = timeit.default_timer()    
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # merge sort
    sample = copy.deepcopy(origin)
    print('merge')    
    start = timeit.default_timer()
    merge.sort(sample)
    stop = timeit.default_timer()    
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # heap sort
    sample = copy.deepcopy(origin)
    print('heap')    
    start = timeit.default_timer()
    heap.sort(sample)
    stop = timeit.default_timer()
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # insertion sort
    sample = copy.deepcopy(origin)
    print('insertion')    
    start = timeit.default_timer()
    insertion.sort(sample)
    stop = timeit.default_timer()
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # shell sort
    sample = copy.deepcopy(origin)
    print('shell')
    start = timeit.default_timer()
    shell.sort(sample)
    stop = timeit.default_timer()
    print(f'Elapsed Time : {stop - start}')