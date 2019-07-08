def solution(A):
    # write your code in Python 3.6
    sum_of_part_one = 0
    sum_of_part_two = sum(A)
    min_difference = None

    for i in range(1, len(A)):
        sum_of_part_one += A[i - 1]
        sum_of_part_two -= A[i - 1]
        difference = abs(sum_of_part_one - sum_of_part_two)
        if min_difference == None:
            min_difference = difference
        else:
            min_difference = min(min_difference, difference)
    return min_difference

def solution1(A):
    B=[]
    j=0
    if A==[] or len(A)==1:
        return 0
    for i in range(0,len(A)-1):
        j=A[i]+j
        diff=sum(A)-(j)
        result=diff-j
        B.append(abs(result))
    return min(B)

print(solution([3,1,2,4,3]))