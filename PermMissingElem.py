def solution1(A):
    i = 1
    if A == []:
        return 1
    elif(len(A)==1):
        n = len(A)
        d = ((n // 2) + 1) * (n+2)
        return abs(d - sum(A))
    else:
        n=len(A)
        d=((n//2)+1)*(n+1)
        return abs(d-sum(A))

def solution(A):
    n = len(A) + 1
    result = n * (n + 1) // 2
    return result - sum(A)
print(solution([1,2,3]))



