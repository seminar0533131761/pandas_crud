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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    help("1")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
