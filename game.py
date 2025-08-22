import numpy as np 
import random                                                                                       #rows  صف 
                                                                                                    #cols عمود                
 
print("========Welcome To The Tic Tac Toe Game========") 
print('The Human is X and the AI is O... Enjoy the game')

# بنسوي لوحة 3×3 كلها خانات فاضية
board = np.full((3, 3), " ") 

# بنطبع اللوحة بشكل مرتب عشان نشوفها
def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

print("This is the game board... \n")
print_board()
print()

# بنحط النقاط حق اللعبين والتعادل
scores = {"X": 0, "O": 0, "Draws": 0}

# اللاعب البني آدم يدخل صف وعمود ويحط X لو الخانة فاضية
def human():
    rows = int(input("Enter number from [rows] (0-2) : "))
    cols = int(input("Enter number from [cols] (0-2) : "))
    print()
    if board[rows][cols] == " ":
        board[rows][cols] = "X"
    else:
        print("Cell already taken, try again.")
        human()

# الكمبيوتر يختار مكان عشوائي فاضي ويحط O
def Ai_player():
    while True:
        rows = random.randrange(3)
        cols = random.randrange(3)
        if board[rows][cols] == " ":
            print(f"The AI player chose the place: [{rows}][{cols}]")
            print()
            board[rows][cols] = "O"
            print_board()
            print()
            break

# بنتحقق إذا في حد كسب عن طريق الصفوف، الأعمدة، أو الأقطار
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            winner(board[i][0])
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            winner(board[0][i])
            return True
    if board[0][0] == board[1][1] == board[2][2] != " ":
        winner(board[0][0])
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        winner(board[0][2])
        return True
    # لو كل الخانات مليانة وما في كسبان بنقول تعادل
    if not np.any(board == " "):
        print("It's a draw!")
        scores["Draws"] += 1
        return True
    return False

# نعلن مين كسب ونزيد له النقاط
def winner(player):
    if player == "X":
        print("The human wins the game!")
        scores["X"] += 1
    else:
        print("The AI wins!")
        scores["O"] += 1

# نشغل اللعبة حركة حركة، ونفحص النتيجة بعد كل خطوة
def start_game():
    while True:
        human()
        if check_winner():
            print_board()  
            print("Scores:", scores)
            break
        Ai_player()
        if check_winner():
            print_board()  
            print("Scores:", scores)
            break

# نقدر نمسح اللوحة ونبدأ من جديد
def reset_board():
    global board
    board = np.full((3, 3), " ")
    print_board()
    print()

# نسأل لو حابب تلعب مرة ثانية أو تخلص اللعبة
def play_again():
    while True:
        new_game = input("Do you want to play again (Yes\\No)? : ").lower()
        if new_game == "yes":
            print('======Let\'s play a new game!======')
            reset_board()
            start_game()
        elif new_game == "no":
            print("The game ended!")
            break
        else:
            print("Please enter yes or no!")

start_game()
play_again()
