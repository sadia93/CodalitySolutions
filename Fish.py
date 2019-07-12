# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    D=[]
    counter=0
    if len(A)==0:
        return 0
    elif len(A)==1:
        return 1
    for i in range(0,len(A)):
        if B[i]==1:
            D.append(A[i])
        else:
            while len(D)!=0:
                if A[i]>D[-1]:
                    D.pop()
                    counter+=1
                elif A[i]<D[-1]:
                    counter+=1
                    break

    return (len(A))-counter


print(solution([  4, 3, 2, 5, 6 ], [1, 0, 1, 0, 1 ]))
print(solution([ 3, 4, 2, 1, 5 ], [1, 0, 0, 0, 0 ]))
print(solution([7, 4, 3, 2, 5, 6 ], [0, 1, 1, 1, 0, 1]))
print(solution([4,3,2,1,5 ], [0, 1, 0,0, 0]))
