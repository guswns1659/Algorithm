"""
인자 x가 n이 되고, 피보나치 순열 중 n번째(x번째) 해당하는 값을 구해라.
피보나치 정의)
x = 3 = n,
f0 = 0
f1 = 1
f2 = f1 + f0
f3 = f2 + f1
...
fn = fn-1 + fn-2

설계 후 테스트)

n =3
return f(2) + f(1) = f(1) + f(0) + 1 = 1 + 0 + 1 = 2

n = 5
return f(4) + f(3) = f(3) + f(2) + f(2) + f(1) = f(2) + 1 + 1 + 1 + 1 = 5

0 1 1 2 3 5 8 13 21 ....

"""
def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return solution(n-1) + solution(n-2)

print(solution(8))
