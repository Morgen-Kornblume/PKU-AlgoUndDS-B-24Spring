# 第二部分计算用递归
def division(rem, lst):
    # rem: 剩余的数 
    # lst: 当前的划分的最后一个数
    if rem == 0:
        return 1
    if rem < 0:
        return 0
    ans = 0
    for i in range(lst+1, rem+1):
        ans += division(rem-i, i)
    return ans

def calc(rem, lst):
    #划分成若干个奇数
    if rem == 0:
        return 1
    if rem < 0:
        return 0
    ans = 0
    for i in range(lst, rem+1, 2):
        ans += calc(rem-i, i)
    return ans

#整数划分问题
while True:
    try:
        n, k = input().split()
    except:
        break
    n = int(n)
    k = int(k)

# 求将 n 划分 k 个正整数的方案数
# dp[i][j] 表示将 i 划分 j 个正整数的方案数
    dp = [[0 for j in range(k+1)] for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i >= j:
                dp[i][j] = dp[i-j][j] + dp[i-1][j-1]

    print(dp[n][k])

print(division(n, 0))

# 求划分成若干奇数
print(calc(n, 1))