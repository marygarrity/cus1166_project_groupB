from flask import Flask, render_template
app = Flask(__name__)
Car =[
{
'user_id': 'Shawn',
'id': '123',
'car_vin':'ABC123',
'model': 'Ford Truck',
'make': '2018',
'color': 'Red',
},
{
'user_id': 'Sarah',
'id': '456',
'car_vin':'TU456',
'model': 'Toyota',
'make': '2016',
'color': 'Black'
}
]
@app.route("/")
def home():
    return render_template('index.html', Car=Car)

@app.route("/userlist")
def home():
    return render_template('user.html', User=User)
