N = int(input())
counter = 0
for i in range(N):
  numbers = []
  a, b, c, d, e, f, g = map(int,input().split())
  if a % 2 == 0:
    numbers.append(a)
  if b % 2 == 0:
    numbers.append(b)
  if c % 2 == 0:
    numbers.append(c)
  if d % 2 == 0:
    numbers.append(d)
  if e % 2 == 0:
    numbers.append(e)
  if f % 2 == 0:
    numbers.append(f)
  if g % 2 == 0:
    numbers.append(g)
  print(sum(numbers), min(numbers))
  