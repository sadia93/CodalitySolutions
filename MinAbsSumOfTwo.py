def solution(A):
    # write your code in Python 2.7
    i, j, minSum = 0, len(A) - 1, 10 ** 10
    A.sort()
    while i <= j:
        sum = A[i] + A[j]
        minSum = min(minSum, abs(sum))
        if sum < 0:
            i += 1
        elif sum > 0:
            j -= 1
        else:
            return 0
    return minSum


print(solution([-8,4,5,-10,3]))