N = int(input())
C = [input() for _ in range(N)]


uniq_set = set()

for c in C:
  if c not in uniq_set and c[::-1] not in uniq_set:
    uniq_set.add(c)

print(len(uniq_set))