import copy


def sort(data):
    frames = [copy.deepcopy(data)]

    for i in range(1, len(data)):        
        
        for j in range(i - 1, -1, -1):
            if data[j + 1] < data[j]:                
                data[j], data[j + 1] = data[j + 1], data[j]

                frames.append(copy.deepcopy(data))
            else:
                break

    frames.append(data)

    return frames
    # print(data)