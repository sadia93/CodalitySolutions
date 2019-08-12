def get_fib_seq_up_to_n(N):
    fib = [0] * (27)
    fib[1] = 1
    for i in range(2, 27):
        fib[i] = fib[i - 1] + fib[i - 2]
        if fib[i] > N:
            return fib[2:i]

def solution(A):
    A.append(1)
    A.insert(0,1)
    F=get_fib_seq_up_to_n(len(A))
    S=[len(A)]*len(A)
    S[0]=0
    for i in range(1,len(A)):
        if A[i]==1:
            for x in F:
                prev=i-x
                if prev >= 0:
                    if S[prev] + 1 < S[i]:
                        S[i] = S[prev] + 1
                else:
                    break
    return S[-1] if S[-1] <len(A) else -1

print(solution([0,0,0,1,1,0,1,0,0,0,0]))