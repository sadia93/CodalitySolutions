def solution(K, A):
    lower_bound = max(A)
    upper_bound = sum(A)

    if K == 1:
        return upper_bound

    if K >= len(A):
        return lower_bound

    while lower_bound <= upper_bound:
        possible_candidate = (lower_bound + upper_bound) // 2
        block_sum = 0
        count = 0
        for elem in A:
            if block_sum + elem > possible_candidate:
                block_sum = elem
                count += 1
            else:
                block_sum += elem

        if count >= K:
            lower_bound = possible_candidate + 1
        else:
            upper_bound = possible_candidate - 1



    return lower_bound



print(solution(3,[2,1,5,1,2,2,2]))