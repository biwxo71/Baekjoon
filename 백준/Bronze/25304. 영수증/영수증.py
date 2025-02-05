total_price = int(input())
total_numb = int(input())
sum = 0
for i in range(1, total_numb + 1):
  price, numb = map(int, input().split())
  sum = sum + price * numb
if sum == total_price:
  print("Yes")
else:
  print("No")
