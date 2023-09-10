def star(N):
    if N == 1:
        return ["*"]
    else:
        lst = []
        K = 4*N-3

        lst.append("*"*K)
        lst.append("*"+" "*(K-2)+"*")

        sub_lst = star(N-1)
        for i in sub_lst:
            lst.append("*"+" "+i+" "+"*")

        lst.append("*"+" "*(K-2)+"*")
        lst.append("*"*K)

        return lst


N = int(input())
star_line = star(N)
for i in star_line:
    print(i)
