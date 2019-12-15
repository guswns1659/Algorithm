
def solution(L, x):
    for L_element in L:
        if L_element >= x:
            L.insert(L.index(L_element), x)
            break
        else:
            if L.index(L_element) != len(L)-1:
                continue
            else:
                L.append(x)
                break
    return print(L)

solution([20, 37, 58, 72, 91], 19)
