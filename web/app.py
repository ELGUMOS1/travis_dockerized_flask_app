# app.py
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
	    
@app.route('/get/<n>')
def get():
	sol = app.query.filter_by(n=n).all()
	return sol
   
if __name__ == '__main__':
    app.run()
