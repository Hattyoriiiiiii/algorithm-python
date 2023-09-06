n, m = map(int, input().split())
s = list(input())
s_out = s.copy()
c_list = list(map(int, input().split()))
m_list = [list() for i in range(m)]
res_list = []

for i, c in enumerate(c_list):
  m_list[c-1].append(i)

for m in m_list:
  if len(m) > 1:
    m_len = len(m) - 1
    tmp_list = []
    tmp_list.append(m[m_len])
    for j in m[:m_len]:
      tmp_list.append(j)
    res_list.append(tmp_list)
  else:
    res_list.append(m)

for m, r in zip(m_list, res_list):
  for i, j in zip(m, r):
    s_out[i] = s[j]
print("".join(s_out))