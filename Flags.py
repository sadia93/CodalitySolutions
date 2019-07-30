def solution(A):
    N = len(A)
    peaks = []
    for i in range(1, N-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            peaks.append(i)
    if len(peaks) == 0:
        return 0
    # the distance for k flags requires k(k-1) distance between first and last flag
    max_flags_possible = len(peaks)
    while max_flags_possible * (max_flags_possible - 1) > (peaks[-1] - peaks[0]):
        max_flags_possible -=1
    for k in range(max_flags_possible, 0, -1):
        flags_set = 1
        distance = 0
        for i in range(1, len(peaks)):
            distance += abs(peaks[i-1] - peaks[i])
            if distance >= k:
                flags_set += 1
                distance = 0
        if flags_set >= k:
            return k
    return 0





print(solution([1,5,3,4,3,4,1,2,3,4,6,2]))