def solution(arr):
    answer = [[]]
    row = len(arr) # 4
    col = len(arr[0]) # 3
    
    m = max(row, col) # 4
    check = [[0]*m for _ in range(m)]
    
    for i in range(len(arr)): # 4
        for idx, num in enumerate(arr[i]):
            check[i][idx] = arr[i][idx]
    return check