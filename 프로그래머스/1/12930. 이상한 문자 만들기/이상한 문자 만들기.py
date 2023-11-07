def solution(s):
    words=s.split(" ")
    rst = []
    
    for w in words:
        nw = ''
        for idx,num in enumerate(w):
            if idx%2==0:
                nw+=num.upper()
            else:
                nw+=num.lower()
        rst.append(nw)
    return " ".join(rst)