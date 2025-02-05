A, B = map(int, input().split())
while A != 0 and B != 0:
  print(A+B)
  A, B = map(int, input().split())

  if A == 0 and B == 0:
    break

