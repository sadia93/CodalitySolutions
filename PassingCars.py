def solution(A):
    N=len(A)
    countzero=0
    pairs=0
    if N<=1:
        return 0
    for i in range(0,N):
        if A[i]==0:
            countzero+=1
        else:
            pairs+=countzero
    if pairs>1000000000:
        return -1
    else:
        return (pairs)

print(solution([0,1,0,1]))
