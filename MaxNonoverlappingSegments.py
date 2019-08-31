def solution(A, B):
    # write your code in Python 3.6
    n=len(A)
    counter=1
    if n<=1:
        return n
    last=B[0]
    for i in range(1,n):
        if A[i]>last:
            counter+=1
            last=B[i]

    return counter




print(solution([1,3,7,9,9],[5,6,8,9,10]))