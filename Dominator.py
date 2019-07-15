# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    size=0
    value=0
    indice=0
    count=0
    for i in range(0,len(A)):
        if size==0:
            size+=1
            value=A[i]
        else:
            if value!=A[i]:
                size-=1
            else:
                size+=1
    candidate=0
    leader=0
    if (size>0):
        candidate=value
    for i in range(0,len(A)):
        if candidate==A[i]:
            count+=1
            indice=i
    if count>(len(A)//2):
        return indice
    else:
        return -1





print(solution([]))