from collections import deque

def solution(tickets):
    tickets.sort(key = lambda x: x[1])
    queue = deque([("ICN", ["ICN"], tickets)]) # 큐에는 (현재 공항, 경로, 남은 티켓 정보) 가 필요합니다.
    
    while queue:
        current_entry, path, remaining_tickets = queue.popleft()
        
        if len(remaining_tickets) == 0:
            return path
        
        for idx, (frm, to) in enumerate(remaining_tickets):
            if frm == current_entry:
                new_remaining_tickets = remaining_tickets[:idx] + remaining_tickets[idx+1:]
                queue.append((to, path + [to], new_remaining_tickets))