def solution(A):
    A.sort()
    N=len(A)
    count=0
    for i in range(0,N):
        if (A[i]-count)>1:
            return count+1
        elif (A[i]-count)<0:
            count=-1
        elif (A[i]-count==0):
            count-=1
        count+=1

    return count+1

print(solution([-1,-3,1,2]))