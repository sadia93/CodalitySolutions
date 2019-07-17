def checkmin(S):
    if 'A' in S:
        return 1
    elif 'C' in S:
        return 2
    elif 'G' in S:
        return 3
    elif 'T' in S:
        return 4
def solution(S, P, Q):
    N=len(P)
    M=len(Q)
    B=[]
    letters=[]
    for i in range(0,N):
        if len(S)==1:
            B.append(checkmin(S))
        elif P[i]==Q[i]:
             R=S[P[i]]
             B.append(checkmin(R))
        else:
            R=S[P[i]:Q[i]+1]
            B.append(checkmin(R))

    return B


print(solution('CAGCCTA', [0], [0]))