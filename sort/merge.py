def sort(data):
    _merge_sort(data, 0, len(data))
    print(data)


def _merge_sort(data, low, high):
    mid = (low + high) // 2
    if high - low > 2:
        _merge_sort(data, low, mid)
        _merge_sort(data, mid, high)
    t_list = []
    i = low
    j = mid

    # merge
    for k in range(low, high):
        if i < mid and (j >= high or data[i] <= data[j]):
            t_list.append(data[i])
            i += 1
        else:
            t_list.append(data[j])
            j += 1

    for k in range(low, high):
        data[k] = t_list[k - low]
