from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Initialize the application
app = Flask(__name__)

#Connect to the DB 
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:password@localhost:3306/DB'

#Avoid Warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#Initialize SQLAchemy and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)


#Defining the Model for Drivers table
class Drivers(db.Model):
    name = db.Column(db.String(100),primary_key=True)
    number = db.Column(db.Integer)
    nationality = db.Column(db.String(50))
    dob = db.Column(db.DateTime)

    def __init_(self,name, number, nationality):
        self.name = name
        self.number = number
        self.nationality = nationality
        self.dob = dob

#Drivers Table Schema
class DriversSchema(ma.Schema):
    class Meta:
        fields = ('name', 'number', 'nationality', 'dob')

#Just one response
drivers_schema = DriversSchema()
#More than one responses
drivers_schema = DriversSchema(many = True)

#Get Driver Table Values
@app.route('/drivers', methods=['GET'])

def get_drivers():
    all_drivers = Drivers.query.all()
    result = drivers_schema.dump(all_drivers)

    return jsonify(result)

#Welcome message
@app.route('/', methods=['GET'])

def index():
    return jsonify({'Message': 'Welcome, the API Server is running'})

#Run the application
if __name__=="__main__":
    app.run(debug=True)