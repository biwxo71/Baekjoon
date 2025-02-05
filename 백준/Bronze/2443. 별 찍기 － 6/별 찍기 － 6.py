N = int(input())
stars = 2 * N - 1
for i in range(0, N, 1):
  print( " " * i + "*" * stars )
  stars = stars - 2