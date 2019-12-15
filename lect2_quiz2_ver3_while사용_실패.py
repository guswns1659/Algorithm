def solution(L, x):
    
    answer = []
    first_num_x = L.count(x)

    if x not in L:
        answer.append(-1)
        print("성공")
        
    else: #(x가 L안에 있다면)
        while len(answer) < first_num_x:
            print(L.index(x))
            answer.append(L.index(x))
            L.insert(L.index(x), x+1)
            L.pop(L.index(x))
            first_num_x +=1
    return print(answer)

solution([64, 72, 83, 72, 54, 72], 72)
