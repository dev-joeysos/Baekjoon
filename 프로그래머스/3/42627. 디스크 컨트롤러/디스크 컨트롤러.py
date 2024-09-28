import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    
    current_time = 0
    total_time = 0
    count = len(jobs)
    
    heap = []
    index = 0
    finished_jobs = 0
    
    while finished_jobs < count:
        while index < count and jobs[index][0] <= current_time:
            heapq.heappush(heap, [jobs[index][1], jobs[index][0]])
            index += 1
        
        if heap:
            job_duration, job_request_time = heapq.heappop(heap)
            current_time += job_duration
            total_time += current_time - job_request_time
            finished_jobs += 1
        else:
            current_time = jobs[index][0]
            
    answer = total_time // count 
    return answer