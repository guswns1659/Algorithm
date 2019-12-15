from ArrayStack import ArrayStack as Stack #module에서 class를 임포트한다. 
"""
infixToPostfix함수
    인자 : splitToken()의 결과값이다. 중위표기법의 요소들 리스트에 들어있는 인자. 예) ['(',123,'+',34,')','*',45]
    리턴값 : 인자를 후위표기법으로 바꾼 값.

인자가 문자열이었던 함수와 다른점
    인자가 리스트이며, 리스트 속 값들이 int, '(', ')', 연산자로 나눠져있음
    결과값도 리스트로 배출해야함.
"""

def infixTopostfix(tokenList):
    prec = {
            '*' : 3,
            '/' : 3,
            '+' : 2,
            '-' : 2,
            '(' : 1
    }

    opStack = Stack()
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

print(infixTopostfix([3,'+',4,'*',2,'-',4,'/',2]))
        


