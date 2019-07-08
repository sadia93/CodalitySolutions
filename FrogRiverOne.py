def solution(X, A):
    N=len(A)
    total=0
    B=[0]*(X+1)
    for k in range(N):
        if B[A[k]]==0:
            total+=1

        if total==X:
            return k

        B[A[k]] =1
    return -1







print(solution(5, [1, 3,5,2]) )