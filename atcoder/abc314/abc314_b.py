n = int(input())
a_list = []
b_list = []
out_list = []
min_num = 37

for i in range(n):
  # c_list.append(input())
  _ = input()
  a_list.append(list(map(int, input().split())))

x = int(input())


for i, a in enumerate(a_list):
  if x in a:
    b_list.append(i)

for b in b_list:
  if min_num >= len(a_list[b]):
    min_num = len(a_list[b])
for b in b_list:
  if min_num == len(a_list[b]):
    out_list.append(b)
print(len(out_list))

for b in b_list:
  if min_num == len(a_list[b]):
    print(b+1, end=" ")
