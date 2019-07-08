def solution_old(A):
    list=A.copy()
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if(A[i]==A[j]):
                if(list.__contains__(A[i]) or list.__contains__(A[j])):
                    list.remove(A[j])
                    list.remove(A[j])
                    if len(list)==1:
                        return(int(list[0]))
    return(int(list[0]))

def solution(A):
    counter=1
    A.sort()
    prev = A[0]
    if len(A) == 1:
        return (int(A[0]))
    for i in range(1,len(A)):
        if(A[i]==prev):
            counter += 1
        else:
            if counter % 2 == 0:
                counter = 1
            else:
                return prev
        prev = A[i]

    return prev



#3,3,7,9,9,9
print(solution([2, 2, 3, 4,4]))