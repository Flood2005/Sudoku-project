from graphics import *
import random
#Importing from the random library allows us to properly randomly generate the random game each time the program runs

def generate_sudoku():
    base = 3
    side = base * base
    nums = random.sample(range(1, side + 1), side)
    #These 3 work together to create the range of what numbers can be randomly generated.
    #Since side always equals 9 the nums function can only produce numbers from 1-9
    board = [[nums[(base * (r % base) + r // base + c) % side] for c in range(side)] for r in range(side)]
    #Board function is used to determine which row and column each generated number is placed in.
    squares = side * side
    #makes sure only 9 boxes are generated for each row/column
    empties = squares * 3 // 4
    for p in random.sample(range(squares), empties):
        board[p // side][p % side] = 0
    #for loop is what is used to find how many squares get filled in with randomly generated numbers
    return board
    #Returns the randomly generated board to use later when crafting the game
def draw_board(win, board, inputs):
   #This function is actually what draws the board, since the sudoku can be generated via the variables but needs a window to be visible
   for i in range(9):
       #9 is number of spaces on board horizontally and vertically, i is horizontal and j is vertical
       for j in range(9):
           if board[i][j] != 0:
               #checks that none of the randomly generated numbers are 0 before performing the following operations
               text = Text(Point(50*j + 25, 50*i + 25), str(board[i][j]))
               #board variable from generate_sudoku() function is accessed
               text.setSize(25)
               text.draw(win)
               #sets font size and draws within window
           else:
               inputs[i][j].draw(win)
               #if the value is 0, draw an input box

def check_solution(board, user_board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != user_board[i][j]:
                return False
    return True
#runs through every column/row to check if there are any empty or duplicated boxes, if there are it returns false
#to show that the solution the player put in was wrong, otherwise if the solution is correct it returns true

def main():
    board = generate_sudoku()
    user_board = [[0 for _ in range(9)] for _ in range(9)]
    # calls function to generate board

    win = GraphWin("Sudoku", 500, 700)
    win.setBackground("white")
    # properly generates window with white background
    inputs = [[Entry(Point(50*j + 25, 50*i + 25), 1) for j in range(9)] for i in range(9)]
    draw_board(win, board, inputs)
    #calls function to draw the board onto the window
    message = Text(Point(250, 650), "")
    message.setSize(20)
    message.draw(win)
    #generates a text box for the indication messsage at the end of the game - checks whether the board is correct after user hits "submit" button
    submit_button = Rectangle(Point(200, 450), Point(300, 490))
    submit_button.setFill("gray")
    submit_button.draw(win)
    submit_text = Text(Point(250, 470), "Submit")
    submit_text.setSize(16)
    submit_text.draw(win)
    #draws a big button to let the user submit the answer

    while True:
        click_point = win.getMouse()
        #How the program gets the input from the user clicking the mouse
        if 200 < click_point.getX() < 300 and 450 < click_point.getY() < 490:
            #How the prgram checks to see if the user is clicking in the generated window
            for i in range(9):
                for j in range(9):
                    #For loops check over each cell that gets generated for the sudoku game
                    if board[i][j] == 0:
                        #if any of the cells, which there will be at the start of the game, it goes into what lets the user input numbers
                        try:
                            num = int(inputs[i][j].getText())
                            #gets and converts the user input into an integer for whatever cell it is entered in
                            if 1 <= num <= 9:
                                user_board[i][j] = num
                            else:
                                message.setText("Please enter numbers from 1 to 9")
                                break

                        except ValueError:
                            message.setText("Please enter numbers from 1 to 9")
                            break
                            # Checks to see if inputed number is in the 1-9 range, if not it breaks the for loop
                        else:
                            break
                        # As a summary this portion of code checks if all inputs are valid for a row
                        # it moves to the next row. If all inputs are valid for all rows, it breaks out of the outer loop
    if check_solution(board, user_board):
        message.setText("Good job!")
        #if the game is successfully completed, this is displayed at the bottom fo the screen
    else:
        message.setText("Game Over. Try again.")
        #If the solution is wrong this text is displayed
    win.getMouse()
    win.close()
    #After displaying either text option, the window closes
main()