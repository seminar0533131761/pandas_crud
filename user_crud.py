from user import User
import pandas as pd


class UserCRUD:
    def __init__(self):
        self.user = {}
        self.users = []
        self.df = pd.read_csv('users.csv')
        ls = self.df.T.to_dict().values()
        for i in ls:
            self.users.append(User(i["id"], i["user_name"], i["permission"]))

    def get_async(self, _id):
        pass
        # for i in self.users:
        #     if i.id == int(_id):
        #         self.user = User(i.id, i.user_name, i.permission)
        #         return self.user

    def get_row_by_id(self, id):
        # Read the CSV file into a DataFrame
        row = self.df.loc[self.df['id'] == id]
        # Filter the DataFrame based on the specified ID
        # self.user=
        st = row.to_string(header=False, index=False)
        lst = st.split(" ")
        return lst

    def add_user(self, _id, user_name, permission):
        # self.user=User(_id,user_name,permission)
        # df = pd.read_csv('users.csv')
        new_row = {'id': int("111"), 'user_name': 'JohnDoe', 'permission': 'regular'}
        self.df = self.df._append(new_row, ignore_index=True)
        self.df.to_csv('users.csv', index=False)
        return "created successfully"

    def get_all(self):
        # self.df = pd.read_csv('users.csv')
        ls = self.df.T.to_dict().values()
        for i in ls:
            self.users.append(User(i["id"], i["user_name"], i["permission"]))
        return self.users
    def update_permission(self,id):
        row_index = self.df.index[self.df['id'] == 8790]
        # self.df.loc[row_index, 'user_name'] = 'yhuda'
        self.df.loc[row_index, 'permission'] = 'super'
        self.df.to_csv('users.csv', index=False)
    def del_user(self,id):
        row_to_delete = self.df[self.df['id'] == 2134].index
        self.df = self.df.drop(row_to_delete)
        self.df.to_csv('users.csv', index=False)
        print(self.df)


a = UserCRUD()
# lst=a.get_all()
# for i in lst:
#     print(i.id)
print(a.del_user(2222))
