def solution(A,N):
    B=[0]*(N)
    maximum=0
    offset=0
    for i in range(0,len(A)):
        if 1<=A[i]<=N:
            B[A[i]-1]=max(offset,B[A[i]-1])+1
            if maximum < B[A[i]-1]:
                maximum = B[A[i]-1]
        elif A[i]==(N+1):
         #   B=[maximum]*(N)
            offset=maximum
    for i in range(0,len(B)):
        if offset>B[i]:
            B[i]=offset
    return B


print(solution([3,4,4,6,1,4,4],5))

#[3, 2, 2, 4, 2],

