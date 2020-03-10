def sort(data):
    total = len(data) - 1
    
    for i in range(total // 2, -1, -1):
        _heapify(data, i, total)
    for i in range(total, 0, -1):
        # 가장 큰 값을 뒤로
        data[0], data[i] = data[i], data[0]
        total -= 1
        _heapify(data, 0, total)
        
    # print(data)
    

def _heapify(data, i, total):
    left_child = i * 2
    right_child = i * 2 + 1
    greater = i

    # 값이 더 큰 child 찾음
    if left_child <= total and data[left_child] > data[greater]:
        greater = left_child
    if right_child <= total and data[right_child] > data[greater]:
        greater = right_child

    if greater != i:
        data[i], data[greater] = data[greater], data[i]
        # 위 노드로
        _heapify(data, greater, total)    

    