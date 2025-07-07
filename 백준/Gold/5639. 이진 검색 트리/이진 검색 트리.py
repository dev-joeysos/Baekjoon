#binary search tree, preoreder, postorder
import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

def postorder(start,end):
    if start>=end:
        return
    
    root=nums[start]
    
    idx=end
    for i in range(start+1,end):
        if nums[i]>root:
            idx=i
            break

    postorder(start+1,idx) # left subtree
    postorder(idx,end) # right subtree
    print(root)

nums=[]
while True:
    line=input()
    if not line:
        break
    nums.append(int(line.strip()))

postorder(0,len(nums))