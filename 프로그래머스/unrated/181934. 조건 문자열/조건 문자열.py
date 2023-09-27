def solution(ineq, eq, n, m):
    check = ineq + eq
    if check == ">=":
        return int(n>=m)
    elif check == "<=":
        return int(n<=m)
    elif check == ">!":
        return int(n>m)
    elif check == "<!":
        return int(n<m)