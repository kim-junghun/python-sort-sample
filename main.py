import random
import timeit

from sort import *


def make_sample_list(high):
    sample = list(range(1, high + 1))
    random.shuffle(sample)
    return sample


if __name__ == '__main__':
    length = 100
    # ---------------------------------------
    # bubble sort
    sample = make_sample_list(length)
    print('bubble')
    start = timeit.default_timer()
    bubble.sort(sample)
    stop = timeit.default_timer()
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # selection sort
    sample = make_sample_list(length)
    print('selection')
    start = timeit.default_timer()
    selection.sort(sample)
    stop = timeit.default_timer()
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # quick sort
    sample = make_sample_list(length)
    print('quick')
    start = timeit.default_timer()
    quick.sort(sample)
    stop = timeit.default_timer()
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # merge sort
    sample = make_sample_list(length)
    print('merge')
    start = timeit.default_timer()
    merge.sort(sample)
    stop = timeit.default_timer()
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # heap sort
    sample = make_sample_list(length)
    print('heap')
    start = timeit.default_timer()
    heap.sort(sample)
    stop = timeit.default_timer()
    print(f'Elapsed Time : {stop - start}')
    # ---------------------------------------
    # ---------------------------------------