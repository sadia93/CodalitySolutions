def solution(A):
    A.sort()
    n=len(A)
    if A[0]!=1:
        return 0
    for i in range(0,n-1):
        if A[i+1]-A[i]==1:
            continue
        else:
            return 0
    return 1




print(solution([2,3]))