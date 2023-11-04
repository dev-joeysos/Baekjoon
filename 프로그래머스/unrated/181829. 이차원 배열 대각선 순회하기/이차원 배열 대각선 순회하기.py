def solution(board, k):
    rst = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            v = i+j
            if v > k:
                continue
            rst += board[i][j]
    return rst