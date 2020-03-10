import argparse
import copy
import random
import sys
import timeit

import sort
# 실제 사용됨 (getattr)
from sort import *


def make_sample_list(high):
    sample = list(range(1, high + 1))
    random.shuffle(sample)
    return sample


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Sorting algorithms')
    parser.add_argument('-l', '--length', help='length of source list')
    parser.add_argument('-t', '--type', action='extend', nargs='+', type=str, help='choose types of sorting')
    parser.add_argument('-a', '--all', help='all sorting. if flagged, -t, --type will be ignored', action='store_true')

    argv = sys.argv[1:]
    args = parser.parse_args(argv)
    print(args)

    if args.length is None:
        length = 100
    else:
        length = int(args.length)

    # algorithm 딕셔너리
    # 이름(str): 순서(int)
    type_dict = {}
    for i in range(len(sort.__all__)):
        type_dict[sort.__all__[i]] = i
    algorithm_count = len(type_dict)

    # 정렬 실행 지시 리스트
    if args.all:
        execution_instruct = [True for _ in range(algorithm_count)]
    else:
        execution_instruct = [False for _ in range(algorithm_count)]
        if args.type is None:
            # 무작위 선택
            execution_instruct[random.choice(range(algorithm_count))] = True
        else:
            type_list = args.type

            for typ in type_list:
                try:
                    execution_instruct[type_dict[typ]] = True
                except KeyError:
                    print(f'목록에 없는 키 "{typ}"는 무시합니다.')

    # print(execution_instruct)

    origin = make_sample_list(length)
    # print(origin)
    for i in range(len(execution_instruct)):
        if execution_instruct[i]:
            sample = copy.deepcopy(origin)
            print('----------------------------------------------')
            print(f'execute {list(type_dict.keys())[i]} algorithm')
            start = timeit.default_timer()
            getattr(globals()[list(type_dict.keys())[i]], 'sort')(sample)
            stop = timeit.default_timer()
            print(f'Elapsed Time : {stop - start}')
            print('----------------------------------------------')
        else:
            continue


