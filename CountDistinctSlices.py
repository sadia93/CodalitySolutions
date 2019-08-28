def solution(M, A):
    mm = [0]*(M+1)
    nb = 0
    nf = 0
    ns = 0
    mr = False
    ln = 0
    for ii in range(len(A)):
        if mm[A[ii]]==0:
            mm[A[ii]] = 1
            ln+=1
            ns+=ii-nb+1
            if ns>1000000000:
                return 1000000000
        else:
            mh = A[ii]
            nf = ii
            while A[nb]!=mh:
                mm[A[nb]] = 0
                nb+=1
            nb+=1
            ns+=ii-nb+1
            #print nb
    return ns


print(solution(6,[3,4,5,5,2]))