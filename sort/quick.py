def sort(data):
    _sort_partition(data, 0, len(data) - 1)
    # print(data)


def _sort_partition(data, low, high):
    if high - low > 0:
        i = low
        j = high
        
        # 피벗, 임의로 가장 앞쪽 선택
        pivot = data[i]
        i += 1

        while i < j:
            # 피벗보다 작은 값 찾음
            while i <= high and data[i] < pivot:
                i += 1
            # 피벗보다 큰 값 찾음
            while j >= low and data[j] > pivot:
                j -= 1
            
            # 작은 값 좌측, 큰 값 우측
            if i < j:
                data[i], data[j] = data[j], data[i]
        
        # 피벗 이동
        if data[low] > data[j]:
            data[low], data[j] = data[j], data[low]

        _sort_partition(data, low, j - 1)
        _sort_partition(data, j + 1, high)