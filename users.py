import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE users (car_model VARCHAR(255), car_vimNum VARCHAR(255))") #user table

#If this page is executed with no error, you have successfully created a table named "user_table"

__tablename__ = "user_table"
__table_args__ = {"schema": "example"} #?

user_id = Column(Integer, primary_key=True, nullable=False)
user_name = Column(String(100), nullable=False)
user_password = Column(String(100), nullable=False)

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
        return ("ID: " + self.user_id + "   Username: " + self.user_name + "   Password: "+ self.user_password)

def main():
    user_id = uuid() #uuid variable?
    user_name = input('Username: ')
    user_password = input('Password: ')
    myuser = users(user_id, user_name, user_password)
    print(myuser.get_user_information())

if __name__ == "__main__":
    main()
