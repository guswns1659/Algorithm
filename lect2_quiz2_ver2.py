# 리스트에서 하나씩 꺼내서 비교한다. x와 같은 값을 찾으면 그 값의 인덱스를 리스트로 만든다. 리스트 끝까지 반복문이 진행되어야 한다.
# 아래 조건에서 정확한 답이 나오려면 인덱스 1의 72가 한번 출력되고, 인덱스 3의 72가 출력되어야 한다. 하지만 72가 같은 값이기에 인덱스 1이 출력된다. 
"""
Key Question : 처음 인덱스 뒤에서부터 자른다음 두번째 i 값 구하고 처음인덱스 값을 더하는거 어떰???

문제
인자로 주어지는 리스트 L 내에서, 또한 인자로 주어지는 원소 x 가 발견되는 모든 인덱스를 구하여 이 인덱스들로 이루어진 리스트를 반환하는 함수 solution 을 완성하세요.

리스트 L 은 정수들로 이루어져 있고 그 순서는 임의로 부여되어 있다고 가정하며, 동일한 원소가 반복하여 들어 있을 수 있습니다. 이 안에 정수 x 가 존재하면 그것들을 모두 발견하여 해당 인덱스들을 리스트로 만들어 반환하고, 만약 존재하지 않으면 하나의 원소로 이루어진 리스트 [-1] 를 반환하는 함수를 완성하세요.

예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 72 인 경우의 올바른 리턴 값은 [1, 3] 입니다.
또 다른 예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 83 인 경우의 올바른 리턴 값은 [2] 입니다.
마지막으로 또 다른 예를 들어, L = [64, 72, 83, 72, 54] 이고 x = 49 인 경우의 올바른 리턴 값은 [-1] 입니다.

"""

#깃에 추가할 Version2
def solution(L, x):
    answer = [] # for문 안에 있으면 for문 돌 때 마다 빈리스트로 새롭게 정의되기 때문이다. 
    for i in L:
        if i == x:
            if answer == []:
                i_index = L.index(i)
                answer.append(i_index)
                continue
            else: #빈리스트가 아닌 경우는 먼저 있는 값의 인덱스가 들어가 있는 경우. 
                 another_i_index = L[L.index(i)+1:].index(i) + (L.index(i)+1) #먼저값 이후 부터 검색할 수 있게 슬라이싱하고 먼저값 인덱스를 더해준다. 이해되니? 
                 answer.append(another_i_index)
                 continue
        else:
            if L.index(i) != len(L) -1: 
                continue
            else:
                if answer == []:
                    answer.append(-1)
                    break
                else:
                    break # break해줘야 for문이 종료된다. 안해주면 계속 대기하고 있을껄? 
    return answer

solution([64, 72, 83, 72, 54], 72)


# 깃에 추가할 Version1 : 같은 값의 인덱스를 구분할 필요성을 느끼기 전 코드.
"""
def solution(L, x):
    answer = []
    for i in L:
        if i == x: 
            i_index = L.index(i)
            answer.append(i_index)
        else:
            if L.index(i) != len(L) -1:
                continue
            else:
                if answer == []:
                    answer.append(-1)
                    break
                else:
                    break
    return print(answer)

solution([64, 72, 83, 72, 54], 72)
"""
