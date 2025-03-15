import random
def num_game():
    num1=int(input("Enter start point: "))
    num2=int(input("Enter end point: "))

    while True:
        user=int(input(f"guess a number from {num1} to {num2} : "))

        random_num=random.randint(num1,num2)

        if user==(random_num):
            print("Correct!!" )
            break
        elif user<random_num:
            print("too low ")

        elif user>random_num:
            print("Too high! ")
    
        
        else:
            print("Correct! ")
            break



def rock_paper_scissor():
    game_choice=["rock","paper","siccors"]
    computer_choice=random.choice(game_choice)
    while True:
        user=input("Enter (Rock, paper or scissors: )")
        lower_user=user.lower()
        if lower_user!=computer_choice:
           print("try again! ")
        else:
            print("Correct!, you win")
            break

while(True):
    print("""Welcome to game!
          1.guess number game
          2.rock paper scissor game
          3.exit
          """)
    user=int(input("Enter your choice"))
    if user==1:
        num_game()
    elif user==2:
        rock_paper_scissor()
    elif user==3:
        print("Exited the program!")
        break
    else:
        print("invalid choice")
     