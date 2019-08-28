# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    # write your code in Python 3.6
    cnt = 0
    current = 0
    for part in A:
        current += part
        if current >= K:
            cnt += 1
            current = 0

    return cnt


print(solution(4,[1,2,3,4,1,1,3]))