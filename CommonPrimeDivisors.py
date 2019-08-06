def gcd(a, b):
	while b > 0:
		a, b = b, a % b
	return a

def common(a, b):
	if b == 1:
		return True
	c = gcd(a, b)
	if c == 1:
		return False
	return common(a, b/c)

def solution(A, B):
	result = 0
	for i in range(0, len(A)):
		if common(A[i], B[i]) and common(B[i], A[i]):
			result += 1
	return result



print(solution([15,10,3],[75,30,5]))