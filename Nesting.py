def solution(S):
    stack=[]
    if len(S)==0:
        return 1
    for i in range(0,len(S)):
        if S[i]=='(':
            stack.append(S[i])
        elif stack!=[] and S[i]==')' and stack[-1]=='(':
                stack.pop()
        else:
            return 0
    if len(stack)!=0:
      return 0
    else:
      return 1


print(solution("())"))

