"""
Key point
-재귀함수의 정의를 정확히 인식하며 풀려고 접근함. 재귀함수란 자기 자신을 다시 호출함. 그러면 인자도 변화가 크게 없다는 걸 의미
-if x not in L[l:u+1]에서 처음엔 L[l:u]으로 슬라이싱했다. 그러니 오류가 나오더라 생각해보니, 슬라이싱할 때는 마지막 인덱스 전까지만 자름
-코드 바로 입력 안하고 손으로 작성하고 생각한다면 코드 입력했다. 귀납적이 아니라 연역적으로 풀기.
"""

def solution(L, x, l, u):
    if  x not in L[l:u+1]: 
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    else:
        return solution(L, x, mid+1, u)

solution([2, 4, 5, 6, 8, 11, 14, 15, 17, 18], 2, 0, 9) #
