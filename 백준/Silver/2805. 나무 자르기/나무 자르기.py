# BS
n, target = map(int,input().split())
trees = list(map(int,input().split()))

def treeSum(h, trees):
    sum = 0
    for tree in trees:
        if tree > h:
            sum += (tree-h)
    return sum
    
def binarySearch(target, trees):
    start, end = 0, max(trees)
    result = 0
    
    while(start<=end):
        mid = (start+end)//2
        # print('start, mid, end, result:', start, mid, end, result) 
        # h를 mid로 설정하고 자른 나무 길이 합이 target 보다 크다면, 나무를 덜 잘랴아 함
        # 즉, target은 h보다 높게 있음
        if treeSum(mid, trees) >= target:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result

print(binarySearch(target, trees))