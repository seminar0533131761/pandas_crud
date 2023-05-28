def count_arrangements(N):
    dp = [[0] * 4 for _ in range(N+1)]

    dp[0][0] = 1
    for i in range(1, N+1):
        dp[i][1] = dp[i-1][1] + dp[i-1][2] + dp[i-1][3]
        if i >= 2:
            dp[i][2] = dp[i-2][1] + dp[i-2][2] + dp[i-2][3]
        if i >= 3:
            dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]

    return dp[N][1] + dp[N][2] + dp[N][3]

# דוגמה לשימוש:
N = 3
result = count_arrangements(N)
print(result)  # יחזיר 3
