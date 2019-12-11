from os.path import join, isfile
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig

################
#### config ####
################
app = Flask(__name__, instance_relative_config=True)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)

from models import Post

def solveNQueens(n):
	sols = []
	def dfs(state, pd, nd):
		r = len(state)
		if r < n:
			for c in range(n):
				if c not in state and c-r not in pd and c+r not in nd:
					dfs(state+[c], pd|{c-r}, nd|{c+r})
		else: 
			sols.append(state)
	
	dfs([], set(), set())
	return sols
	
# Drop all of the existing database tables
db.drop_all()

# Create the database and the database table
db.create_all()

# Insert  data
for i in range(1,5):
	temp = str(solveNQueens(i))
	sol = Post(n = i, sol = temp)
	db.session.add(sol)
	db.session.commit()
	    
@app.route('/get/<n>')
def index(n):
    sol = Post.query.filter_by(n=n).all()
    return str(sol)

@app.route("/")
def home():
    return "Hello, World!"
	        
if __name__ == '__main__':
    app.run()
