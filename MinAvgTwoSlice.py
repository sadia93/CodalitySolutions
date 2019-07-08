def solution(A):
    min=10001
    min_id=None
    for i in range(0,len(A)):
        if i < (len(A)-1) and (A[i]+A[i+1])/2 < min:
            min=(A[i]+A[i+1])/2
            if min_id==None:
                min_id=i
            elif min_id<i:
                min_id=i
        if i < (len(A)-2) and (A[i]+A[i+1]+A[i+2])/3<min :
            min = (A[i] + A[i + 1] + A[i+2]) / 3
            if min_id == None:
                min_id = i
            elif min_id < i:
                min_id = i
        if i < (len(A)-3) and (A[i]+A[i+1]+A[i+2]+A[i+3])/4<min :
            min = (A[i] + A[i + 1] + A[i+2] + A[i+3]) / 4
            if min_id == None:
                min_id = i
            elif min_id < i:
                min_id = i
        if i < (len(A) - 4) and (A[i] + A[i + 1] + A[i + 2] + A[i + 3]+A[i+4])/5 < min:
            min = (A[i] + A[i + 1] + A[i + 2] + A[i + 3]+A[i+4]) / 5
            if min_id == None:
                min_id = i
            elif min_id < i:
                min_id = i
        if i < (len(A) - 5) and (A[i] + A[i + 1] + A[i + 2] + A[i + 3]+ A[i + 4]+ A[i + 5])/6 < min:
            min = (A[i] + A[i + 1] + A[i + 2] + A[i + 3]+ A[i + 4]+ A[i + 5]) / 6
            if min_id == None:
                min_id = i
            elif min_id < i:
                min_id = i

    print(min_id)


solution([4,2,2,5,1,5,8])