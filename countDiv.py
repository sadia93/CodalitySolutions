# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    counter=0
    R=A//K

    M=B//K
    if (A%K)==0:
      return (M-R)+1
    else:
        return (M-R)


    return counter


def solution1(A, B, K):
    # write your code in Python 3.6
    counter=0
    if (K==1):
        return ((B+1)-A)
    while A<=B:
        if (A%K)==0:
            A=K*A
            counter += 2
        else:
            A+=1
    return (counter+1)



print(solution(0, 0, 2))