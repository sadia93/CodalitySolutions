def solution(A):
    # write your code in Python 3.6
    maxprofit=0
    sale=0
    if len(A)==0 or len(A)==1:
        return 0
    bought = A[0]
    for i in range(0,len(A)):
        bought=min(bought,A[i])
        maxprofit=max(maxprofit,A[i]-bought)
    return maxprofit

print(solution([]))

#print(solution([23171,21011,21123,21366,21013,21367]))

