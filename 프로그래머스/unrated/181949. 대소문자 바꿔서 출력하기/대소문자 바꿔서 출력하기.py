str = input()
a = ''

for x in str:
    if x == x.lower():
        a = a + x.upper()
    else:
        a= a + x.lower()
print(a)

