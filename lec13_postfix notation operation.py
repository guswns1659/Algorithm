"""
후위표기볍 연산하는 알고리즘 미리 생각해보기
인자 = '3+4*2-4/2'를 str으로 넣고 for문 돌려서 i가 연산자, 괄호가 아니면 int로 casting해서 answer.append(i)하기.
연산자 만났는데, 우선순위 비교하고 opStack.pop() 하는 곳에
if oper == '*':
K = answer.pop(-2) * answer.pop(-1)
answer.append(K)
elif oper == '/':
K = answer.pop(-2) / answer.pop(-1)
answer.append(K)
elif oper == '+':
K = answer.pop(-2) + answer.pop(-1)
answer.append(K)
else: 
K = answer.pop(-2) - answer.pop(-1)
answer.append(K)
위 연산자 부르는 코드를 삽입한다.
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

#S = '3+4*2-4/2'
#S2 = '(3+(4-2))*2'

def solution(S): 
    opStack = ArrayStack()
    answer = []
    
    for i in S:       
        if i not in '+-*/':
            if i not in '()':
                answer.append(int(i))
            elif i == '(':
                opStack.push(i)
            else: 
                while opStack.peek() !='(': 
                    oper = opStack.pop()
                    if oper == '*':
                        K = answer.pop(-2) * answer.pop(-1)
                        answer.append(K)
                    elif oper == '/':
                        K = answer.pop(-2) / answer.pop(-1)
                        answer.append(K)
                    elif oper == '+':
                        K = answer.pop(-2) + answer.pop(-1)
                        answer.append(K)
                    else: 
                        K = answer.pop(-2) - answer.pop(-1)
                        answer.append(K)
                    continue
                opStack.pop()
                continue
        else: 
            if not opStack.isEmpty():
                while prec[opStack.peek()] >= prec[i]:
                    oper = opStack.pop()
                    if oper == '*':
                        K = answer.pop(-2) * answer.pop(-1)
                        answer.append(K)
                    elif oper == '/':
                        K = answer.pop(-2) / answer.pop(-1)
                        answer.append(K)
                    elif oper == '+':
                        K = answer.pop(-2) + answer.pop(-1)
                        answer.append(K)
                    else: 
                        K = answer.pop(-2) - answer.pop(-1)
                        answer.append(K)
                        
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
        if oper == '*':
            K = answer.pop(-2) * answer.pop(-1)
            answer.append(K)
        elif oper == '/':
            K = answer.pop(-2) / answer.pop(-1)
            answer.append(K)
        elif oper == '+':
            K = answer.pop(-2) + answer.pop(-1)
            answer.append(K)
        else: 
            K = answer.pop(-2) - answer.pop(-1)
            answer.append(K)
    return answer[0]

S ='(3+(4-2))*2'
# answer = 10.0

print(solution(S))






