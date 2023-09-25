import heapq
def solution(scoville, K):

    answer = 0
    heapq.heapify(scoville)
    lenheap = len(scoville)
    while (scoville):
        x = heapq.heappop(scoville)
        if len(scoville) == 0 and x < K:
            answer = -1
            break
        if x < K:
            y = heapq.heappop(scoville)
            z = x + y*2
            heapq.heappush(scoville, z)
            answer += 1
    return answer
'''
최소 횟수
여기 힙을 어캐 쓸지 고민

최소 뽑아 작아 
또 뽑아서 곱햇
곱해서 다시 넣어 근데 이 리스트는 힙으로 삽입

heap 빌 때까지 반복
'''
