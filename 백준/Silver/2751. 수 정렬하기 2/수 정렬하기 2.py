# 수 정렬2
import sys
# 오름차순 정렬
N = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(N)]
arr.sort()
sys.stdout.write('\n'.join(map(str, arr)) + '\n')
