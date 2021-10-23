from flask import Flask, redirect, url_for, request, render_template
from flask import jsonify
import uuid
import time
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def home():
   d = 'Hi from test API'
   return jsonify(d)

class User(db.Model):
   id = db.Column(db.String(200), primary_key=True,nullable=False)
   num1=db.Column(db.Integer, nullable=False)
   num2=db.Column(db.Integer, nullable=False)
   answer=db.Column(db.Integer,nullable=True)


@app.route('/calculate/<number1>/<number2>', methods =["GET", "POST"])
def send(number1,number2):
   # id = unique_identifier
   # value = {num1,num2,unique_identifier}
   unique_identifier = str(uuid.uuid4())
   user = User(id=unique_identifier, num1 = int(number1), num2 = int(number2))
   db.session.add(user)
   db.session.commit()
   return jsonify(unique_identifier)

@app.route('/get_answer/<identifier>')
def index(identifier):
   user = User.query.filter_by(id=identifier).first_or_404()
   if(user.answer==None):
      # time.sleep(10)
      ans = user.num1 + user.num2
      user.answer = ans
      db.session.commit()
      return jsonify("please Wait")
   return jsonify(user.answer)


if __name__ == '__main__':
   app.run(debug = True)

