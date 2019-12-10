from os.path import join, isfile
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


################
#### config ####
################
app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

@app.route('/get/<n>')
def index():
    sol = app.query.filter_by(n=n).all()
    return sol
    
if __name__ == '__main__':
    app.run()
