#반올림 연산
def round_up_half(num):
    if num>0:
        return int(num+0.5)
    else:
        return int(num-0.5)
    
n=int(input())
op=[]
for _ in range(n):
    op.append(int(input()))
rm_n=round_up_half(n*0.15)
op.sort()
print(round_up_half(sum(op[rm_n:n-rm_n:1])/(n-rm_n*2)) if n!=0 else 0)