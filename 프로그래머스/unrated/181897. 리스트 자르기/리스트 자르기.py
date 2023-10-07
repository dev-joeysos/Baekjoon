def solution(n, s, nl):
    a,b,c = s[0], s[1], s[2]
    
    if n==1:
        return nl[:b+1]
    elif n==2:
        return nl[a:]
    elif n==3:
        return nl[a:b+1]
    else:   
        return nl[a:b+1:c]