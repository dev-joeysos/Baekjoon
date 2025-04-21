# 시험 감독
'''
필요한 감독관의 최소 수를 구하는 문제
'''
center=int(input())
examinees=list(map(int,input().split()))
general,manager=map(int,input().split())

answer=0

for examinee in examinees:
    # 총감독관 1명은 무조건 필요
    answer+=1
    examinee-=general
    if examinee>0:
        # 부감독 수 계산 (올림 처리)
        answer+=(examinee+manager-1)//manager

print(answer)