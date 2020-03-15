import copy


def sort(data):
    frames = [copy.deepcopy(data)]

    _merge_sort(data, 0, len(data), frames)

    frames.append(data)

    return frames
    # print(data)


def _merge_sort(data, low, high, frames):
    mid = (low + high) // 2
    if high - low > 2:
        _merge_sort(data, low, mid, frames)
        _merge_sort(data, mid, high, frames)

    frames.append(copy.deepcopy(data))

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

    frames.append(copy.deepcopy(data))