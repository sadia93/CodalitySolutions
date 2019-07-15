def solution(H):
    s=[]
    stone=0
    i=0
    while i<len(H):
        if len(s)!=0 and H[i]<s[-1]:
            while(len(s)!=0 and H[i]<s[-1]):
                s.pop()
            i-=1
        elif len(s)!=0 and s[-1]==H[i]:
            pass
        else:
            stone+=1
            s.append(H[i])
        i+=1
    return stone


print(solution([8,8,5,7,9,8,7,4,8]))