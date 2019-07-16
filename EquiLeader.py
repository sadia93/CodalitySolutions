# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

    # write your code in Python 3.6


def solution(A):
    leader1=0
    leader2=0
    countL=0

    size = 0
    value = 0
    indice = 0
    count = 0
    for i in range(0, len(A)):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1
    candidate = 0
    if (size > 0):
        candidate = value
    for i in range(0, len(A)):
        if candidate == A[i]:
            count += 1
    if count > (len(A) // 2):
        leader1 = candidate
    else:
        leader1 = None
    if leader1 is None:
        return 0
    countR=count
    for i in range(0,len(A)):
        if leader1==A[i]:
            countL+=1
            countR-=1
        if countL>(i+1)//2 and countR>(len(A)-i-1)/2:
            leader2+=1
    return leader2



print(solution([4,3,4,4,4,2]))