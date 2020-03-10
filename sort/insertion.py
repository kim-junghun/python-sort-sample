def sort(data):
    for i in range(1, len(data)):        
        
        for j in range(i - 1, -1, -1):
            if data[j + 1] < data[j]:                
                data[j], data[j + 1] = data[j + 1], data[j]
            else:
                break                
    # print(data)