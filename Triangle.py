# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    for i in range(0,len(A)-2):
        if A[i]+A[i+1]>A[i+2]:
            if A[i]+A[i+2]>A[i+1]:
                if A[i+1]+A[i+2]>A[i]:
                    return 1

    return 0


print(solution([10,50,5,1]))