"""
Point
맨 처음 내가 설계한 코드가 안되서 강의 중 강사님의 설계대로 코드 구현해도 마지막 테스트 7,8이 안됐다.
그러다 질문하려고 들어갔는데, 누군가 예외케이스를 언급했다. 이 케이스는 내 코드도 구현 못하는 케이스였다. 
A+B*C-D/E 였는데, 이게 뭐가 문제냐면 스택에 연산자가 있으면 i와 스택 속 연산자랑 비교하는데, 한번 하고도
뒤에 연산자가 남아있으면 다시 우선순위를 비교해야했다. 그 코드 짜는게 까다로웠다. 마지막 집중해서 결국 완성했다!!! 으자자자
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
        else: 
            if not opStack.isEmpty():
                while prec[opStack.peek()] >= prec[i]:
                    oper = opStack.pop()
                    answer += oper
                    if opStack.isEmpty():
                        #opStack.push(i) 여기서 break하면 while를 나가서 opStack.push(i) 코드가 작동한다.
                        break 
                    else:
                        continue
                opStack.push(i)
                continue
            else:
                opStack.push(i)
                continue
    while not opStack.isEmpty():
        oper = opStack.pop()
        answer += oper
    return answer

S = 'A+B*C-D/E'
# answer = AB+CD+*

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




