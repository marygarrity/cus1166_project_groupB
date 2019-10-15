from sqlalchemy import Table, Column, Integer, String, MetaData
meta = MetaData()

users = Table('users', meta,
    Column('user_id', Integer, primary_key = True),
    Column('user_name', String),
    Column('user_password', String),
)#users table

meta.create_all(engine)

CREATE TABLE users(
    user_id INTEGER NOT NULL,
    user_name VARCHAR,
    user_password VARCHAR,
    PRIMARY KEY (user_id)
)

class users:

    def __init__(self, user_id, user_name, user_password):
        self.user_id = user_id
        self.user_name = user_name

    def set_user_id(self, user_id):
        self.user_id = user_id

    def set_user_name(self, user_name):
        self.user_name = user_name

    def set_user_password(self, user_password):
        self.user_password = user_password

    def get_user_id(self):
        return self.user_id

    def get_user_name(self):
        return self.user_name

    def get_user_password(self):
        return self.user_password

    def get_user_information(self):
        return ("ID: " + self.user_id + "   Username: " + self.user_name + "   Password: " + self.user_password)

def main():
    user_id = uuid() #uuid variable?
    user_name = input('Username: ')
    user_password = input('Password: ')
    myuser = users(user_id, user_name, user_password)
    print(myuser.get_user_information())

if __name__ == "__main__":
    main()
