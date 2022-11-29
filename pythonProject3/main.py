def check(arr,q, x):
    d = arr[q + 1] - arr[q]
    j = 0
    for i in range(n):


n = int(input())

arr = map(int, input().split())
q = int(input())
for i in range(q):
    first = 0
    last = n + 1
    to = int(input())
    while(first <= last):
        mid = first + (last - first) // 2
