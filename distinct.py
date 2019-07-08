# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if A==[]:
        return 0
    A.sort()
    counter=1
    for i in range(0,len(A)-1):
        if A[i]!=A[i+1]:
            counter+=1

    return counter


print(solution([1,1,1,1]))