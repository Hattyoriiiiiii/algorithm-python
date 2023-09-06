N, P, Q = input().split()
D = list(map(int, input().split()))

sum_price_disc = int(Q) + min(D)
if int(P) < sum_price_disc:
  print(P)
else:
  print(sum_price_disc)