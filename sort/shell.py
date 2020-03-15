import copy


def sort(data):
    frames = [copy.deepcopy(data)]

    gap = len(data) // 2

    while gap >= 1:
        if gap % 2 == 0:
            gap += 1

        for i in range(gap):
            for j in range(i + gap, len(data), gap):
                for k in range(j, i, -gap):
                    if data[k] < data[k - gap]:
                        data[k], data[k - gap] = data[k - gap], data[k]
                    frames.append(copy.deepcopy(data))

        gap = gap // 2

    frames.append(data)

    return frames
    # print(data)
