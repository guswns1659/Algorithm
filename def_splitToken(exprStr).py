#exprStr = 중위표현식인 문자
def splitToken(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        elif c in '0123456789':
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

print(splitToken('(123+45) * (231+45)'))
#['(',123,'+',45,')','*','(',231,'+',45,')']
