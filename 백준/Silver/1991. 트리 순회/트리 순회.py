# tree,recursion
from collections import defaultdict
import sys
input=sys.stdin.readline
n=int(input())
d_tree=defaultdict(list)
for _ in range(n):
    root,left,right=input().split()
    d_tree[root]+=[left,right]

def preorder(node): #root->left->right
    if node=='.':
        return
    print(node,end='')
    preorder(d_tree[node][0])
    preorder(d_tree[node][1])
    
def inorder(node): #left->root->right
    if node=='.':
        return
    inorder(d_tree[node][0])
    print(node,end='')
    inorder(d_tree[node][1])
    
def postorder(node): #left->right->root
    if node=='.':
        return
    postorder(d_tree[node][0])
    postorder(d_tree[node][1])
    print(node,end='')

root='A'
preorder(root)
print()
inorder(root)
print()
postorder(root)