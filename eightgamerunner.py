import eightgame as game

gameBoard = game.create_board([0, 1, 2, 3, 4, 5, 6, 7, 8])
game.display_board(gameBoard)

while True:
    try:
        user_input = int(input("Enter a valid move"))
    except ValueError:
        print("Invalid Input try again")
        continue

 #   move = tuple(int(item) for item in user_input.split(" "))
    move = game.position_of_number(gameBoard, user_input)

    try:
        updatedgameBoard = game.result(gameBoard, move)
    except:
        print("Invalid Move try again")
        continue
    
    game.display_board(updatedgameBoard)
    if game.game_over(updatedgameBoard):
        print("Game over")
        break
    else:
        gameBoard = updatedgameBoard
