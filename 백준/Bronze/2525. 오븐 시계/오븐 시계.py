H, M= map(int,input().split())
T = int(input())
if M + T >= 60:
  H = ((M + T) // 60 + H) % 24
  M = (M + T) % 60
  print(H, M)
elif M + T < 60:
  M = M + T
  print(H, M)