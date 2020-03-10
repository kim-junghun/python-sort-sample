def sort(data):
    
    gap = len(data) // 2

    while gap >= 1:
        if gap % 2 == 0:
            gap += 1

        for i in range(gap):
            for j in range(i + gap, len(data), gap):
                for k in range(j, i, -gap):
                    if data[k] < data[k - gap]:
                        data[k], data[k - gap] = data[k - gap], data[k]

        gap = gap // 2

    print(data)
