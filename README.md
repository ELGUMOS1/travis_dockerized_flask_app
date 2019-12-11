# travis_dockerized_flask_app
Simple dockerized python flask app
The source code is in the web directory, the main app is the app.py file.
The database was built using postgres and is composed just by a 'n' and its solutions 'sol'.
The solution to the EightQueensPuzzle was found in leetcode by WangQiuc.
We can use an array to express a game state. Each index indicate queue's row and each value indicate queue's column.
e.g. [1,3,0,2] expressed a game state as:

".Q.."
"...Q"
"Q..."
"..Q."
The solution was saved in this format to avoid saving extra characters.

