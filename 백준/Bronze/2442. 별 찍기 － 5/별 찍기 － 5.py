N = int(input())
stars = 1
for i in range(N-1, -1, -1):
  print(i * " " + "*" * stars)
  stars += 2

