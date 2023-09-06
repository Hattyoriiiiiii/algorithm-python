n, m, p = map(int, input().split())

val = ((n - m) / p) + 1
if val < 1:
  print(int(0))
else:
  print(int(val))