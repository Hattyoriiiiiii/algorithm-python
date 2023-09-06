N = int(input())
A = list(map(int, input().split()))
A = sorted(A)

n_start = A[0]
n_end = n_start + N

for a in range(n_start, n_end + 1):
  if a not in A:
    print(a)