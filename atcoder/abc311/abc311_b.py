N, D = map(int, input().split())

cnt = 0

schedule_list = [list(map(str, input().split())) for l in range(N)]
all_list = [0] * D

for s in schedule_list:
  for i in range(D):
    if s[0][i] == "o":
      all_list[i] += 1
    else:
      pass

cnt = 0
cnt_max = 0

for i in all_list:
  if i == N:
    cnt += 1
    if cnt_max < cnt:
      cnt_max = cnt
  else:
    cnt = 0

print(cnt_max)