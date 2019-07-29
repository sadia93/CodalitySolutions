def solution(A):
  peaks = []
  length = len(A)
  for i in range(1, length-1):
    if A[i-1] < A[i] > A[i+1]:
      peaks.append(i)

  count = len(peaks)
  if count == 0:
    return 0

  for i in range(count, 0, -1):
    if len(A) % i == 0:
      blockSize = length // i
      found = [0] * i
      foundCount = 0
      for peak in peaks:
        blockIndex = peak // blockSize
        if found[blockIndex] == 0:
          found[blockIndex] = 1
          foundCount += 1

      if foundCount == i:
        return i

  return 0

print(solution([1,2,3,4,3,4,1,2,3,4,6,2]))
