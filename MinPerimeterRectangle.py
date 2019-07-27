def solution(N):
    i=1
    minPerimeter=None
    Perimeter=0
    while (i*i<N):
        if (N%i==0):
            Perimeter=2*(i+(N//i))
            if minPerimeter==None:
                minPerimeter = Perimeter
            elif Perimeter<minPerimeter:
                minPerimeter=Perimeter
        i+=1
    if ((i*i)==N):
        Perimeter=2*(i+i)
        if minPerimeter == None:
            minPerimeter = Perimeter
        elif Perimeter < minPerimeter:
            minPerimeter = Perimeter
    return minPerimeter


print(solution(1))