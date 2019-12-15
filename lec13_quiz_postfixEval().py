"""
강의 듣기전 혼자서 후위표기법 연산 알고리즘을 완성해봤다.
이 때 도전이 실습 문제를 빠르게 풀 수 있게 도와줬다. 
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


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for token in tokenList:
        if type(token) == int:
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            while opStack.peek() != '(':
                oper = opStack.pop()
                postfixList.append(oper)
            opStack.pop()
        else:
            if not opStack.isEmpty():
                while prec[opStack.peek()] >= prec[token]:
                    oper = opStack.pop()
                    postfixList.append(oper)
                    if opStack.isEmpty():
                        break
                    else:
                        continue
                opStack.push(token)
            else:
                opStack.push(token)
    while not opStack.isEmpty():
        oper = opStack.pop()
        postfixList.append(oper)
    return postfixList
    


def postfixEval(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }
    opStack = ArrayStack()
    for i in tokenList:
        if type(i) == int:
            opStack.push(i)
        elif i == '*':
            later = opStack.pop()
            faster = opStack.pop()
            data = faster * later
            opStack.push(data)
        elif i == '/':
            later = opStack.pop()
            faster = opStack.pop()
            data = faster / later
            opStack.push(data)
        elif i == '+':
            later = opStack.pop()
            faster = opStack.pop()
            data = faster + later
            opStack.push(data)
        elif i == '-':
            later = opStack.pop()
            faster = opStack.pop()
            data = faster - later
            opStack.push(data)
    answer = opStack.pop()
    return answer

    
def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val

print(solution('((4+5)+4 ) * 3'))
