from app import db
from models import Solutions

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
for i in range(1,15):
	temp = str(solveNQueens(i))
	sol = Solutions(n = i, sol = temp)
	db.session.add(sol)
	db.session.commit()
	    
#
print('...done!')
