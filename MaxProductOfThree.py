# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    return max(A[-1]*A[-2]*A[-3],A[0]*A[1]*A[2],A[0]*A[1]*A[-1])




print(solution([-3, -2, 1,2,5,6]))

