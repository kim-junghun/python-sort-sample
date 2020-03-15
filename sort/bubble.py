import copy


def sort(data):

    frames = [copy.deepcopy(data)]

    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

            frames.append(copy.deepcopy(data))
    # print(data)
    frames.append(data)
    return frames