from sqlalchemy import Table, Column, Integer, String, MetaData
meta = MetaData()

cars = Table('cars', meta,
    Column('car_model', String),
    Column('car_vimNum', Integer, primary_key = True),
)#cars table

meta.create_all(engine)

CREATE TABLE cars( #SyntaxError: invalid syntax ???
    car_model VARCHAR,
    car_vimNum INTEGER NOT NULL,
    PRIMARY KEY (car_vimNum)
)

#FORIEGN KEY:
user_id = Column(
    Integer,
    ForeignKey('user.id', ondelete = 'CASCADE'),
    nullable = False,
    #no need to add index=True, all FKs have indexes
)
user = relationship('User', backref = 'clients')

class cars:

    def __init__(self, car_model, car_vimNum):
        self.car_model = car_model
        self.car_vimNum = car_vimNum

    def set_car_model(self, car_model):
        self.car_model = car_model

    def set_car_vimNum(self, car_vimNum):
        self.car_vimNum=car_vimNum

    def get_car_model(self):
        return self.car_model

    def get_car_vimNum(self):
        return self.car_vimNum

    def get_car_information(self):
        return ("Car name: " + self.car_model + "   Vim Number: " + self.car_vimNum)

def main():
    car_model = input('Enter car model: ')
    car_vimNum = input('Enter vim number: ')
    mycar = cars(car_model, car_vimNum)
    print(mycar.get_car_information())

if __name__ == "__main__":
    main()
