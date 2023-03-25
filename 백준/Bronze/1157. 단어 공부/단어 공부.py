a_small = [chr(i) for i in range(97, 123)]
a_large = [chr(i) for i in range(65, 91)]
count_s = [0]*26
count_l = [0]*26
count_total = [0]*26
N = input()
for c in N:
    if c in a_small:
        count_s[ord(c) - ord('a')] += 1
    elif c in a_large:
        count_l[ord(c) - ord('A')] += 1

for i in range(26):
    count_total[i] = count_s[i] + count_l[i]

max_value = max(count_total)

if count_total.count(max_value) > 1:
    print('?')
else:
    index = count_total.index(max_value)
    print(chr(index+ord('A')))