N, _ = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]

judge_list = []

for i in range(N):
  Pi = C[i][0]
  # P_num = C[i][1]
  Fi = C[i][2:]
  # print(Fi)
  for j in range(N):
    if j != i:
      Pj = C[j][0]
      Fj = C[j][2:]
      Fj_uniq = len(set(Fj) - set(Fi))
      if (Pi >= Pj) & (set(Fj).issuperset(set(Fi))) & ((Pi > Pj) or (Fj_uniq >= 1)):
        judge_list.append("Yes")
        break
      else:
        judge_list.append("No")
    else:
      pass

if "Yes" in judge_list:
  print("Yes")
else:
  print("No")