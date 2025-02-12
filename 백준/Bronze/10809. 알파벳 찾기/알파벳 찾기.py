s = input()
alp = [-1] * 26
for i in range(len(s)):
  if alp[ord(s[i]) - ord("a")] == -1:
        alp[ord(s[i]) - ord("a")] = i

print(*alp)