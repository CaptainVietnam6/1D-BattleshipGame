from random import randint
ship_location = randint(0,9)
ship_board = ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*",]
ship_board_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print(*ship_board)
print(*ship_board_num)
user_shot = ""
isValidInput = False
while isValidInput == False:
    user_shot = input("Where do you want to shoot?: ")
    if user_shot.isnumeric():
        user_shot = int(user_shot)
        if user_shot >= 0 and user_shot <= 9:
            isValidInput = True
        elif user_shot > 9 or user_shot < 0:
            print("Please enter a number between 0-9 for your shot!")
            isValidInput = False
            print(*ship_board)
            print(*ship_board_num)
    else:
        print("Please enter a numeric value between 0-9, not letters or words!")
isCorrectShot = False
if user_shot != ship_location:
    isCorrectShot = False
while isCorrectShot == False:
    ship_board[user_shot] = "M"
    print(*ship_board)
    print(*ship_board_num)
    print("Please try again!")
    isValidInput = False
    while isValidInput == False:
        user_shot = input("Where do you want to shoot?: ")
        if user_shot.isnumeric():
            user_shot = int(user_shot)
            if user_shot >= 0 and user_shot <= 9:
                isValidInput = True
            elif user_shot > 9 or user_shot < 0:
                print("Please enter a number between 0-9 for your shot!")
                isValidInput = False
                print(*ship_board)
                print(*ship_board_num)
        else:
            print("Please enter a numeric value between 0-9, not letters or words!")
    if user_shot == ship_location:
        isCorrectShot = True
    if isCorrectShot == True:  
        ship_board[user_shot] = "H"
        print(*ship_board)
        print(*ship_board_num)
        print("Congrats! You sank the ship! It was located at [" + str(ship_location) + "]")
