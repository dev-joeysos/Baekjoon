def solution(n, wires):
    min_val = n  # 최대 차이는 n-1일 수 있으므로 n으로 초기화

    for wire in wires:
        # 네트워크를 나눌 두 집합
        networkA, networkB = set(), set()
        temp = wire

        # 전선을 임시로 제거한 후 복사본 생성
        temp_wires = wires[:]
        temp_wires.remove(wire)

        # 네트워크 A, B에 초기 노드 배정
        networkA.add(temp[0])
        networkB.add(temp[1])

        # 네트워크를 확장해 나가기 위한 탐색 (BFS와 유사한 방식)
        change = True
        while change:  # 변화가 있을 때까지 반복
            change = False
            for w in temp_wires:
                # 네트워크 A에 연결된 노드가 있으면 추가
                if w[0] in networkA or w[1] in networkA:
                    if w[0] not in networkA or w[1] not in networkA:
                        networkA.add(w[0])
                        networkA.add(w[1])
                        change = True
                # 네트워크 B에 연결된 노드가 있으면 추가
                elif w[0] in networkB or w[1] in networkB:
                    if w[0] not in networkB or w[1] not in networkB:
                        networkB.add(w[0])
                        networkB.add(w[1])
                        change = True

        # 두 네트워크의 차이 계산
        diff = abs(len(networkA) - len(networkB))
        min_val = min(min_val, diff)

    return min_val
