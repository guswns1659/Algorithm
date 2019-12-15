"""
문제 해결 key point
-for문 과 while문 중 고민했고, 이진탐색이기에 while로 했다. for문이라면 x랑 L의 element랑 하나씩 비교하는 선형탐색이 되기에 효율성이 떨어진다.
-강사님이 while의 True 조건을 제시해줬기에 쉽게 풀 수 있었다. 없었다면 가장 어려줬을 조건이다.
    왜 while 조건은 lower < higher가 아니라 lower <= higher 일까? 아래 식을 보자
    x=2인 경우 이진탐색을 계속하면 lower = higher = 0으로 같아진다. 그러니 두 값이 같아지는 조건도 True가 되어야 값을 구할 수 있음.
       ex)  L = [2, 3, 5, 6, 9, 11, 15, 16, 17, 19, 21, 22, 34, 54] 
            middle = 15
            middle = 5
            middle = 2
            x = 2
"""
def solution(L, x):
    answer = 0
    
    if x not in L:
        answer = -1
    else:
        lower = 0
        higher = len(L) -1
        middle = (lower + higher) // 2

        while lower <= higher:
            if L[middle] > x:
                higher = middle -1
                middle = (lower + higher) // 2
                continue
            elif L[middle] < x:
                lower = middle +1
                middle = (lower + higher) // 2
                continue
            else:
                answer = middle
                break
    return print(answer)

solution([2, 3, 5, 9, 11, 15, 31, 34, 45], 34)
