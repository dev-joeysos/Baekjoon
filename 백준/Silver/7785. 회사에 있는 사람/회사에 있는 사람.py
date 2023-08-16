import sys
n = int(input())
namerge = set()
for _ in range(n):
    name, action = sys.stdin.readline().split()
    if action == 'enter':
        namerge.add(name)
    else:
        namerge.discard(name)

sorted_namerge = sorted(namerge, reverse=True)
for member in sorted_namerge:
    sys.stdout.write(member + '\n')