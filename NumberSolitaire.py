def solution(A):
    max_so_far = [A[0]] * (len(A) + 6)
    for index in range(1, len(A)):
        max_so_far[index + 6] = max(max_so_far[index : index + 6]) +A[index]
    return max_so_far[-1]

print(solution([1,-2,0,9,-1,-2]))