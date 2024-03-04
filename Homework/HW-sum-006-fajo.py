cost = []
n,m = map(int,input().split())

def calc(lim) -> bool:
    global cost, m
    nowa = 0
    used = 1
    for tmp in cost:
        if(nowa + tmp <= lim):
            nowa += tmp
        else:
            used += 1
            nowa = tmp
    return (used <= m)
maxx = 0
for i in range(n):
    tmp = int(input())
    cost.append(tmp)
    maxx = max(maxx,tmp)
lower_bound = maxx
upper_bound = 1000000000
while lower_bound < upper_bound:
    mid = (lower_bound + upper_bound) // 2
    if calc(mid) == True:
        upper_bound = mid
    else:
        lower_bound = mid + 1
print(lower_bound)