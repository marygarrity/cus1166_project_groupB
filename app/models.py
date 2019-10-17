from flask_sqlalchemy import SQLAchemy
db = SQLAchemy()
#from app import db 

class User(db.Model):
    #__tablename__ = 'User'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True, nullable = False)
    cars = db.relationship('Car', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.name}')"

class Car(db.Model):
    __tablename__ = 'Car'
    id = db.Column(db.Integer, primary_key = True)
    car_vin = db.Column(db.String(17), unique = True, nullable = False)
    Model = db.Column(db.String(20), nullable = False)
    Make = db.Column(db.String(20), nullable = False)
    Color = db.Column(db.String(20), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Car('{self.car_vin}', '{self.Make}', '{self.Model}',' {self.Color}')"
