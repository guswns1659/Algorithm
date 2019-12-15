#binary search 알고리즘 구현
"""
인자 L은 원소의 값이 순차적인 선형배열이다.
"""

def binarySearch(L, x):
    if x not in L:
        return - 1
    else:
        lower = 0
        higher = len(L) -1
        mid = (lower + higher) // 2
        while lower <= higher:
            if x < L[mid]:
                higher = mid -1
                mid = (lower + higher) // 2
            elif x > L[mid]:
                lower = mid + 1
                mid = (lower + higher) // 2
            else:
                return mid
                
