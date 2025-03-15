def prime_no(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
def Sum_prime():
    lower = int(input("Enter num 1: "))
    upper = int(input("Enter num 2: "))
    sum=0
    for i in range (lower,upper+1):
        if prime_no(i):
            sum+=i
    print("Sum of all prime numbers are: ",sum)


def unit_convert():
    print("1.Meter")
    print("2.feet")
    user=int(input("Enter meter or feet: "))   
    num=int(input("Enter a value: "))
    if user==1:
        meter=num*3.2804
        print(f'Your unit in feet is: {meter}')
    elif user==2:
        feet=num*0.3048
        print(f'Your unit in meter is: {feet}')



def counter():
    user=(input("Enter a word: "))
    count=0
    vowel="AEIOUaeiou"
    for i in user:
        if i.isalpha() and i not in vowel:
            count+=1
    print("Consonant count: ", count) 



    
list_no=[]
def min_max():
    list_no.clear()
    user_input=int(input("Enter total list of number: "))
    for i in range(user_input):
        num=int(input(f"Enter values {i+1}: "))
        list_no.append(num)
    print(list_no)

    print("Minimum: ",min(list_no))
    print("maximun: ",max(list_no))


def palindrome():
    user=input("Enter a string: ")
    user1=user[::-1]
    if user==user1:
        print(f'{user} is a palardome')
    else:
        print(f"{user} is not a paladrome")

def wordcounter():
    string=input("Enter a sentence: ")
    counter=string.split()
    print("Total word: ",len(counter))




while True:
    print("Menu: ")
    print("1. Prime number sum calculator ")
    print("2. Convert length between meters and feet")
    print("3. Count consonants in a string")
    print("4. Find min and max in a list")
    print("5. Check palindrome")
    print("6. Count occurrences of words in file")
    print("7.Exit")

    user_choice=int(input("Enter your choice: "))
    if user_choice==7:
        print("Exited the program: ")
        break
    if user_choice==1:
        Sum_prime()
    elif user_choice==2:
        unit_convert()
    elif user_choice==3:
        counter()
    elif user_choice==4:
        min_max()
    elif user_choice==5:
        palindrome()
    elif user_choice==6:
        wordcounter()
       
    else:
        print("invalid")
        break


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
     