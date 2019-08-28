def solution(A):
    n = len(A)
    A.sort()
    count = 0
    for i in range(0, n - 2):
        k = i + 2
        for j in range(i + 1, n):
            while (k < n and A[i] + A[j] > A[k]):
                k += 1
            if (k > j):
                count += k - j - 1

    return count


print(solution([10,2,5,1,8,12]))