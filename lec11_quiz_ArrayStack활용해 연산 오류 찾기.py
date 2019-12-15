"""
우선 아쉽다.. '(A+B' 케이스를 처리하지 못해서 고민하고 있었는데,
안풀려서 다른 사람 코드 봄..ㅜ 
point: return에 boolean을 출력하는 함수를 넣어도 된다. return은 True 아니면 False라고 생각만 
"""
from ArrayStack_ADT import ArrayStack

def solution(expr):
    match = {')' : '(', '}' : '{', ']' : '['}
    S = ArrayStack()
    for c in expr:
        if c in '({[':
            S.push(c)
        elif c in match:
            if S.isEmpty() :
                return False
            else:
                t = S.pop()
                if t != match[c]:
                    return False
    return S.isEmpty()

S = ArrayStack()
expr = '{A+B)'
print(solution(expr))
