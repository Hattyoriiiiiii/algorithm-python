N = int(input())

mat = []
for n in range(N):
  tmp = []
  line = str(input())
  for i in range(N):
    tmp.append(line[i])
    # tmp.append(int(line[i]))
  mat.append(tmp)

ans = mat.copy()
iter_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]

i, j = 0, 0

# for s in range(len(iter_list)):
#   for _ in range(N-1):
#     next_i = i + iter_list[s][0]
#     next_j = j + iter_list[s][1]
#     print(i, j, mat[i][j], next_i, next_j, ans[next_i][next_j])
#     ans[next_i][next_j] = mat[i][j]
#     i, j = next_i, next_j

for i_val, j_val in iter_list:
  for _ in range(N-1):
    next_i = i + i_val
    next_j = j + j_val
    print(i, j, mat[i][j], next_i, next_j, ans[next_i][next_j])
    ans[next_i][next_j] = mat[i][j]
    i, j = next_i, next_j

# print(ans)

# for j in range(N):
#   print(str("".join(ans[j])))
# print(ans)