def solution(N):
    peaks=0
    totalpeaks=0
    maxpeakscount=None
    A=[]
    if len(N)==1:
        return 0
    for i in range(1,len(N)-1):
        if N[i]>N[i-1] and N[i]>N[i+1]:
            A.append(N[i])
            peaks+=1
    totalpeaks=peaks
    while peaks!=0:
        j=0
        i=0
        if (len(N)%(len(N)//(peaks)))==0:
            BlocksSize=(len(N)//(peaks))
            peakscount=0
            while j<len(N):
                if A[i] in (N[j:j+BlocksSize]):
                    peakscount+=1
                else:
                    break
                i+=1
                j+=BlocksSize
            if maxpeakscount==None:
                maxpeakscount=peakscount
            else:
                if maxpeakscount<peakscount:
                    maxpeakscount=peakscount
        else:
            break
        peaks-=1
    if totalpeaks == 0 :
        return 0
    elif maxpeakscount==None:
        return 1
    elif totalpeaks>=maxpeakscount:
        return maxpeakscount
    else:
        return 1


#(1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2)
print(solution([0,1,0,1,0,1,0,1,0,1,0]))

#print(solution([1,2,3,4,3,4,1,2,3,4,6,2]))

