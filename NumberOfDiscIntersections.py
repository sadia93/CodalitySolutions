def solution(A):
    # write your code in Python 3.6
    #counter=0
    numberofopendiscs=0
    Open=[]
    Closed=[]
    counter=0
    if A==[] or len(A)==1:
        return 0
    for i in range(0,len(A)):
        a = (i) - A[i]
        b = (i) + A[i]
        Open.append(a)
        Closed.append(b)
    Open.sort()
    Closed.sort()
    #print("open=",Open)
    #print("close=",Closed)
    i=0
    j=0
    while i<len(A):
        if Open[i]<=Closed[j]:
            numberofopendiscs+=1
            if numberofopendiscs>1:
                counter+=(numberofopendiscs-1)
            i+=1
        else:
            numberofopendiscs-=1
            j+=1
    if  counter > 10000000:
        return -1
    else:
        return counter


print(solution([1, 5, 2, 1, 4, 0]))