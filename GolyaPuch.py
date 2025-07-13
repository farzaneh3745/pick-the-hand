import random

while True:
    game_count=int(input("Please enter count of play :"))
    counter=0
    user_score=0
    pc_score=0

    while counter < game_count: 
        print(f"-------------------Round {counter+1} ----------------")
        computer_hand=random.randint(0,1)
        user_hand=int(input("Choose left(0) or right(1) hand :"))

        if computer_hand == user_hand:
            print("You win")
            user_score+=1
        else:
            print("Compure win")
            pc_score+=1

        counter+=1

    print(f"computer = {pc_score} - user = {user_score}")

    if input("Do you want to restart[Y/N] ? ").upper()=="N":
        break
print("Goodbye")
