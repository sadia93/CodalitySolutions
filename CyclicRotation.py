def solution(A, K):
    if len(A)==1 or A==[]:
        return A
    while K>0:
        B = []
        B.append(A[-1])
        for i in range(0,len(A)-1):
            B.append(A[i])
        A=B
        K-=1

    return A



A = [3, 8, 9, 7, 6]
K = 3
print(solution([3, 8, 9, 7, 6], 2) )

