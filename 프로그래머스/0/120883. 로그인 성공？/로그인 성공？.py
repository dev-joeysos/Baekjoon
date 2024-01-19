def solution(id_pw, db):
    answer = ''
    '''
    id, pw가 모두 일치한다 = "login"을 return한다.
    else: fail
    아이디만 일치 "wrong pw"
    '''
    ide = id_pw[0]
    pw = id_pw[1]
    for i in range(len(db)):
        if ide == db[i][0]:
            if pw == db[i][1]:
                return "login"
            else:
                return "wrong pw"
    else:
        return "fail"
    return answer