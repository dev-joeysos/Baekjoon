def solution(data, col, row_begin, row_end):  
    data.sort(key = lambda x: [x[col-1], -x[0]])
    
    S_i = []
    for i in range(1,len(data)+1):
        sum = 0
        for item in data[i-1]:
            sum += item % i
        S_i.append(sum)
        
    x = S_i[row_begin-1]
    for i in range(row_begin, row_end):
        x = x^S_i[i]

    return x