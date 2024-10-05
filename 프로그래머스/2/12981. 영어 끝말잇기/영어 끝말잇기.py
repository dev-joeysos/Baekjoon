def solution(n, words):
    used_words = set()  
    last_letter = words[0][0]  

    for i, word in enumerate(words):
        player_num = (i % n) + 1 
        turn = (i // n) + 1  

        # 중복된 단어를 말했거나, 단어가 이전 단어의 마지막 글자와 연결되지 않으면 탈락
        if word in used_words or word[0] != last_letter:
            return [player_num, turn]
        
        used_words.add(word)  # 사용된 단어를 추가
        last_letter = word[-1]  # 마지막 글자를 업데이트

    return [0, 0]  