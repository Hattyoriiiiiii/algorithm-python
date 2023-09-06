N = int(input())
S = str(input())

uniq_set = set()
i = 0

for s in S:
  if s not in uniq_set:
    uniq_set.add(s)
  i += 1
  
  if len(uniq_set) == 3:
    break

print(i)