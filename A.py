n, k = map(int, input().split())
a = list(map(int, input().split()))

breed_map = {}
next_id = 0

for i in range(n):
    x = a[i]
    if x not in breed_map:
        breed_map[x] = next_id
        next_id += 1
    a[i] = breed_map[x]

freq = [0] * next_id
uniq = 0
l = 0
ans = 0

for r in range(n):
    if freq[a[r]] == 0:
        uniq += 1
    freq[a[r]] += 1

    while uniq > k:
        freq[a[l]] -= 1
        if freq[a[l]] == 0:
            uniq -= 1
        l += 1

    length = r - l + 1
    if length > ans:
        ans = length

print(ans)