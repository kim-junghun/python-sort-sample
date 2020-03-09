def sort(data):
    for i in range(len(data) - 1):
        least = i
        # 최소값 찾음
        for j in range(i + 1, len(data)):
            if data[j] < data[least]:
                least = j

        if i != least:
            data[i], data[least] = data[least], data[i]
    print(data)