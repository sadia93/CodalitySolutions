def solution(N):
    result=0
    binarynumber=bin(N)
    maxlist=[]
    binarynumber=binarynumber.rstrip("0")
    if (len(binarynumber)<=4):
        return 0
    else:
        for i in range(2,len(binarynumber)):
            if(binarynumber[i])=="1":
                if(i==len(binarynumber)-1):
                    return max(maxlist)
                j=i
                result=0
                while binarynumber[j+1]!="1" and j<len(binarynumber)-2:
                    result+=1
                    j+=1
                maxlist.append(result)
            else:
                None




print(solution(1041))
