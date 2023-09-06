n = input().split(" ")

ans = int(n[1]) - int(n[0])
thre = int(n[1]) + int(n[0])

if thre < 6 or (thre > 7 and thre < 13) or thre > 13:
  if ans == 1:
    print("Yes")
  else:
    print("No")
else:
  print("No")