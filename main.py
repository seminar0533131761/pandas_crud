# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def help(_id):
    df = pd.read_csv('users.csv')
    df = pd.DataFrame(df)
    new_row = {'id': int(456), 'user_name': 'ggh', 'permission': 'regular'}
    df = df._append(new_row, ignore_index=True)
    print(df)


def max_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n  # יצירת מערך עזר עם ערכי התחלה של 1
    max_length = 1

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                max_length = max(max_length, dp[i])

    return max_length

# דוגמה לשימוש:
arr = [3, 10, 2, 1, 20]
result = max_increasing_subsequence(arr)
print(result)  # יחזציר 3

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   max_increasing_subsequence(arr)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
