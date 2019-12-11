# travis_dockerized_flask_app
Simple dockerized python flask app using postgres, flask, nginx and Flask-SQLAlchemy
The source code is in the web directory, the main app is the app.py file.
The database was built using postgres and is composed by a single table 'solutions' composed by 2 columns 'n' and its solutions 'sol'.
The solution to the EightQueensPuzzle is in the app.py, this solution was proposed by WangQiuc in leetcode.
We can use an array to express a game state. Each index indicate queue's row and each value indicate queue's column.
e.g. [1,3,0,2] expressed a game state as:

".Q.."
"...Q"
"Q..."
"..Q."
The solution was saved in this format to avoid saving extra characters.
The tests just check if in all the solutions at list 3 or 2 solutions match with the expected results.
This repository was build based on this repo https://github.com/realpython/orchestrating-docker from realpython.
