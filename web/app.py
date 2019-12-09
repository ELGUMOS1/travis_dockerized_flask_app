# app.py
from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from models import *

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
	
@app.route('/', methods=['POST'])
def post():
	for i in range(1,10):
	    temp = str(solveNQueens(i))
	    sol = Post(n = i, sol = temp)
	    db.session.add(sol)
	    db.session.commit()
		
	    
@app.route('/get/<n>')
def get():
	sol = app.query.filter_by(n=n).all()
	return sol
   
if __name__ == '__main__':
    app.run()
