"""
문제 풀 수 있던 포인트들
-if x in L : 힌트2를 보고 생각함. 만약 x가 L에 없으면 바로 L.append(-1)하면 계산이 빨라짐.
-pop()을 생각함. 슬라이싱은 2개까지는 괜찮은데 3개 이상부터 복잡해짐. 여기서 사고하는데 오래걸림.
pop()은 사고하다가 어느순간 나왔을텐데, 그보다 먼저 강사님이 이미 수업 도중에 말했다.
상수시간인 메소드가 pop()과 append()라고 그럼 프로그램의 복잡성을 줄이려면 이 둘을 사용하는게 포인트 
"""
def solution(L, x):
    
    answer = []

    if x not in L: # x가 L에 없다면
        answer.append(-1)
    else:  # x가 있다면
        for L_element in L:
            if L_element != x:
                continue
            else:        
                answer.append(L.index(x))
                L.insert(L.index(x), x+1) #x 자리에 +1한 값을 넣는다. 
                L.pop(L.index(x)) # 첫번째 x를 뺀다.
    return print(answer)

solution([64, 72, 83, 72, 54, 72, 72, 72], 72)

