import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  passwd="mypassword",
  database="mydatabase"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE cars (car_model VARCHAR(255), car_vimNum VARCHAR(255))") #car table

#If this page is executed with no error, you have successfully created a table named "car_table"

__tablename__ = "car_table"
__table_args__ = {"schema": "example"} #?

car_vimNum = Column(Integer, primary_key=True, nullable=False)
car_model = Column(String(100), nullable=False)

#FORIEGN KEY:
user_id = Column(
    Integer,
    ForeignKey('user.id', ondelete='CASCADE'),
    nullable=False,
    # no need to add index=True, all FKs have indexes
    )
user = relationship('User', backref='clients')

class cars:

    def __init__(self, car_model,car_vimNum):
        self.car_model = car_model
        self.car_vimNum = car_vimNum

    def set_car_model(self,car_model):
        self.car_model = car_model

    def set_car_vimNum(self,car_vimNum):
        self.car_vimNum=car_vimNum

    def get_car_model(self):
        return self.car_model

    def get_car_vimNum(self):
        return self.car_vimNum

    def get_car_information(self):
        return ("Car name "+ self.car_model +" Vim Number "+self.car_vimNum)

def main():
    car_model = input('Enter car model: ')
    car_vimNum = input('Enter vim number: ')
    mycar = cars(car_model,car_vimNum)
    print(mycar.get_car_information())

if __name__ == "__main__":
    main()
