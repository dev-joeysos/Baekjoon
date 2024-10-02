def solution(n, times):
    answer = 0
    start = 0 
    end = n * max(times)
    
    while True:
        mid = (start + end) // 2
        total = 0
        
        for time in times:
            total += mid // time
        
        if total > n:
            end = mid - 1
        elif total < n:
            start = mid + 1
        else:
            return mid