import time

def rec(n):
    if n <=1:
        return n
    else:
        return rec(n-1) + rec(n-2)

def iter(n):
    a = 0
    b = 1
    count = 0
    if n<=1:
        return n
    else:
        while count < n-1:
            count +=1
            c = b + a
            a = b
            b = c
        return b #return이 while문 안에 들어가있으면 한번 while문 실행하고 return 보이니까 바로 출력한다. 
    
while True:
    number = int(input("input number..."))

    ts = time.time()
    rec(number)
    rec_elapsedTime = time.time() - ts
    print("{0:.3f}".format(rec_elapsedTime))
    
    ts = time.time()
    iter(number)
    rec_elapsedTime = time.time() - ts
    print("{0:.3f}".format(rec_elapsedTime))
