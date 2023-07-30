N, B = map(int, input().split())
result = []
while N > 0:  # 나눠지지 않을 때까지
    R = N % B  # R = 나머지
    N = N // B
    if R < 10:
        result.append(str(R))
    else:
        result.append(chr(ord('A') + R - 10))

print(''.join(result[::-1]))