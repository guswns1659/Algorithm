"""
문제: 괄호 2개까진 함수가 작동하는데, 3개부터 값의 오류가 있음.
"""
class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}
"""
연산속도가 느려서 테스트 실패인지 의문이 들었다.
강의 속 알고리즘 설계대로 괄호와 연산자도 구분한다.
    피연산자면 그냥 출력
    '('이면 스택에 push
    ')'이면 '(' 나올 때까지 스택에서 pop, 출력
    연산자이면 스택에서 우선순위 체크
"""


def solution(S): #self는 안들어간다. 메서드가 아니기 때문이다. 
    opStack = ArrayStack()
    answer = ''
    
    for i in S:       
        if i not in '+-*/':
            if i not in '()':
                answer += i
            elif i == '(':
                opStack.push(i)
            else: #닫는 괄호라면
                while opStack.peek() !='(': #opStack.peek()으로 한 이유는 pop()으로 할경우 조건 확인하면서 스택의 값이 사라지니 oper에 담을 수 없다.
                    oper = opStack.pop()
                    answer += oper
                    continue
                opStack.pop()
                continue
        else: #연산자 만나면
            if opStack.isEmpty():
                opStack.push(i)
                continue
            else: #스택에 연산자가 있다면
                while not opStack.isEmpty():
                    if prec[opStack.peek()] >= prec[i]: #스택의 마지막 연산자가 i보다 우선순위가 높거나 같다면
                        oper = opStack.pop()
                        answer += oper
                            if opStack.isEmpty():
                                opStack.push(i)
                            else:
                                continue
                    if 
                    else: #스택의 마지막 연산자가 i보다 우선순위가 낮다면
                        opStack.push(i)
                    
    if opStack.isEmpty(): #수식이 끝나고 스택이 비어있으면
        return answer
    else: #수식이 끝나고 스택이 비어있지 않다면
        while not opStack.isEmpty():
            oper = opStack.pop()
            answer += oper
        return answer

S = '(A+(B-C))*D'
# answer = ABC**DE*FB+*+

print(solution(S))


"""
우선순위 : {'(' : 1, '+' : 2, '-' : 2, '*' : 3, '/' : 3}
for 문을 돌려 인자 S에서 꺼낸 원소를 i에 저장한다.                            
    1. 피연산자면 answer에 추가하기
    2. 연산자, 괄호 만나면
        스택.isEmpty() 면 스택.push()
        스택.isEmpty() 아니면
            만약 ')' 라면
                while 스택.size() !=0:
                    opStack.peek()가 '(' 아니면 스택.pop() 한 뒤 answer에 추가
                    opStack.peek()가 '(' 면 pop() 해서 버린다.
                반복문 끝나면 ')'도 버림. (None 처리?) -> 꼭 필요한가? continue
            만약 스택 마지막 연산자가 크고 같은데
                만약 스택 밖 연산자 == '(' 면
                    스택 밖 괄호를 스택.push()
                아니면
                    스택 마지막 연산자 pop() 하고 출력한다.
                    스택 밖 연산자를 스택.push()
            스택 마지막 연산자가 작다면
                만약 스택 마지막 연산자 == '(' 면
                    스택 밖 연산자를 스택.push()
                아니면
                    스택 밖 연산자를 출력
    3. 연산이 끝나면
            스택.isEmpty()라면 끝
            스택.isEmpty() 아니면 스택.pop()해서 answer에 추가
                    
""" 




