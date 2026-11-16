import sys
from collections import defaultdict

n = int(input())
a = [int(x) for x in input().split()]

if n == 1:
    print("1")
    sys.exit(0)

cnt = 1
past_nums = defaultdict(int)
past_nums[a[0]] = 1
for i in range(1, len(a)):
    curr = a[i]
    cnt += i - past_nums[curr]
    past_nums[curr] += 1

print(cnt)
