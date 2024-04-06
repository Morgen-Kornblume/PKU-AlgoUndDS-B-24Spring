# import numpy as np

def dp1(n, k, memo1):  # 整数为n拆成k份
    if memo1[n][k] != -1:
        return memo1[n][k]
    if n == k:
        return 1
    if k == 1:
        return 1
    if n >= k + k:
        memo1[n][k] = dp1(n - k, k, memo1) + dp1(n - 1, k - 1, memo1)
    else:
        memo1[n][k] = dp1(n - 1, k - 1, memo1)
    return memo1[n][k]

def dp2(n, choose, cost, memo2):  # 从前choose个整数里挑，凑成n
    if n == 0:
        return 1
    if choose == 0:
        return 0
    if n >= cost[choose - 1]:
        memo2[n][choose] = dp2(n - cost[choose - 1], choose - 1, cost, memo2) + dp2(n, choose - 1, cost, memo2)
    else:
        memo2[n][choose] = dp2(n, choose - 1, cost, memo2)
    return memo2[n][choose]

cost = [i for i in range(55)]
while True:
    try:
        n, k = input().split()
    except:
        break
    n = int(n)
    k = int(k)
    memo1 = [[-1 for j in range(55)] for i in range(55)]
        
    print(dp1(n, k, memo1))  # 问题1
    memo2 = [[-1 for j in range(55)] for i in range(55)]
    print(dp2(n, n, cost, memo2))  # 问题2
        # N划分成若干个奇正整数之和的划分数目
        # dp[i][j]代表i划分成j个奇正整数之和的数目
    dp = [[-1 for j in range(55)] for i in range(55)]
    for i in range(1, n + 1):
            if i % 2:
                dp[i][1] = 1
            else:
                dp[i][1] = 0
    for i in range(2, n + 1):
            for j in range(2, i + 1):
                if i >= 2 * j + j:
                    dp[i][j] = dp[i - 2 * j][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1]
    cnt = sum(dp[n][1:n + 1])
    print(int(cnt))
