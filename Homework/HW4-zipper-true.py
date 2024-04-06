n = int(input())

for k in range(n):
    str1, str2, str3 = input().split()
    l1 = len(str1)
    l2 = len(str2)
    l3 = len(str3)
    # 初始化一个二维数组 (l1+1)*(l2+1) 用于存储状态
    dp = [[False for j in range(l2+1)] for i in range(l1+1)]
    dp[0][0] = True
    for i in range(l1+1):
        for j in range(l2+1):
            if i > 0:
                dp[i][j] = dp[i][j] or (dp[i-1][j] and str1[i-1] == str3[i+j-1])
            if j > 0:
                dp[i][j] = dp[i][j] or (dp[i][j-1] and str2[j-1] == str3[i+j-1])
    print("Data set %d: %s" % (k+1, "yes" if dp[l1][l2] else "no"))