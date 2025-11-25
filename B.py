import math


n, k = map(int, input().split())
y = list(map(int, input().split()))

L = [0] * (2*n)
R = [0] * (2*n)

for i in range(n+1, 2*n):
    l, r = map(int, input().split())
    L[i] = l
    R[i] = r

nv = [0] * (2*n)
cv = [0] * (2*n)


for i in range(1, n+1):
    nv[i] = 1
    cv[i] = y[i-1]

for i in range(n+1, 2*n):
    nv[i] = nv[L[i]] + nv[R[i]]
    cv[i] = cv[L[i]] + cv[R[i]]

INF = 1e100
DP = [ [INF]*(n+1) for _ in range(2*n) ]

for i in range(1, n+1):
    DP[i][1] = 0.0

for i in range(n+1, 2*n):
    p = cv[i] / nv[i]
    if p == 0 or p == 1:
        cut_cost = 0.0
    else:
        cut_cost = -p*math.log(p) - (1-p)*math.log(1-p)

    DP[i][1] = cut_cost

    for tL in range(1, nv[L[i]]+1):
        if DP[L[i]][tL] >= INF:
            continue
        for tR in range(1, nv[R[i]]+1):
            if DP[R[i]][tR] >= INF:
                continue
            t = tL + tR
            if t <= nv[i]:
                val = DP[L[i]][tL] + DP[R[i]][tR]
                if val < DP[i][t]:
                    DP[i][t] = val

root = 2*n - 1
print(DP[root][k])