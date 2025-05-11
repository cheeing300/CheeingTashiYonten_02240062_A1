import random

class GuessNumberGame:
    
    def __init__(self):
        self.EASY_LEVEL_ATTEMPTS = 11
        self.HARD_LEVEL_ATTEMPTS = 6
        self.number = random.randint(1, 100)  # The number to guess
        self.attempts = 0
        self.total_guesses = 0  # Total guesses made
        self.valid_guesses = 0  # Count of valid guesses (within 1 to 100)


    def set_difficulty(self, level_chosen):  # Set the number of attempts based on the chosen difficulty level
        if level_chosen == "easy":
            self.attempts = self.EASY_LEVEL_ATTEMPTS
        else:
            self.attempts = self.HARD_LEVEL_ATTEMPTS

    def check_number(self, guessed_number):  # Check the guessed number against the actual number
        
        if guessed_number < self.number:
            print("Your guess is too low.")
            return False
        elif guessed_number > self.number:
            print("Your guess is too high.")
            return False
        else:
            print("Congratulations! You've guessed correctly!")
            return True  # Correct guess

    def play(self):
        
        level = input("Choose the level of difficulty... Type 'easy' or 'hard': ").lower()
        self.set_difficulty(level)
        guessed_number = 0
        
        while guessed_number != self.number and self.attempts > 0:
            print(f"You have {self.attempts} attempts remaining to guess the number.")
            guessed_number = int(input("Guess a number: "))
            if self.check_number(guessed_number):
                break
            self.attempts -= 1
        
        if self.attempts == 0 and guessed_number != self.number:
            print(f"Sorry, GAME OVER. The number was {self.number}.")
            print(f"Total guesses made: {self.total_guesses}")
            print(f"Valid guesses made: {self.valid_guesses}")
        else:
            print("Hooray! You won the game!")
            print(f"Total guesses made: {self.total_guesses}")
            print(f"Valid guesses made: {self.valid_guesses}")


import random

class RockPaperScissors:
    
    def __init__(self):
        self.choices = ("rock", "paper", "scissors")
        self.wins = 0  # Track the number of player wins
    

    def play(self):
        while True:
            person = None
            bot = random.choice(self.choices)
            
            while person not in self.choices:
                person = input("Enter a choice (rock, paper, scissors) or type 'quit' to exit: ").lower()
                
                if person == 'quit':
                    print(f"Thanks for playing! Goodbye! Total wins: {self.wins}")
                    return
            
            print(f"Person: {person}")
            print(f"Bot: {bot}")

            if person == bot:
                print("It's a draw!")
            elif (person == "rock" and bot == "scissors") or \
                 (person == "paper" and bot == "rock") or \
                 (person == "scissors" and bot == "paper"):
                self.wins += 1
                print("Congratulations, you win!...You will receive your prize through mail!")
            else:
                print("Sorry, you lose! Better luck next time Senor")

            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thank you for playing....Do visit again!")
                print(f"Total wins: {self.wins}")  # Show total wins when ending session
                break

class TriviaPursuit:
    def __init__(self):
        self.questions = ["Which fish can walk on land?: ",
            "Which bird cannot fly?: ",
            "Which breed of dog cannot bark?: ",
            "Which animal is back from extinction?: ",
            "Which animal is the cutest?: "]
            
        
        self.options = [("A. mudskipper", "B. Mackerel", "C. Salmon", "D. Swordfish"),
            ("A. Penguin", "B. Kiwi", "C. Finches", "D. Loon"),
            ("A. Chow Chow", "B. Yorkshire Terrier", "C. Basenji", "D. Chihuahua"),
            ("A. Mammoth", "B. Dinosaur", "C. Dire wolf", "D. Dodo"),
            ("A. Quokka", "B. Lowka", "C. Koka", "D. Toka")]
            
        
        self.answers = ["A", "A", "C", "C", "A"]

    def play(self):
        guesses = []
        score = 0
        
        for i, question in enumerate(self.questions):
            print("----------------------")
            print(question)
            for option in self.options[i]:
                print(option)

            guess = input("Enter (A, B, C, D): ").upper()

            while guess not in ["A", "B", "C", "D"]:
                print("Invalid input. Please enter one of the options: A, B, C, or D.")
                guess = input("Enter (A, B, C, D): ").upper()

            guesses.append(guess)
            if guess == self.answers[i]:
                score += 1
                print("CORRECT!")
            else:
                print("INCORRECT!")
                print(f"The correct answer was {self.answers[i]}.")

        print("----------------------")
        print("       RESULTS        ")
        print("----------------------")
        print("Answers: ", " ".join(self.answers))
        print("Your guesses: ", " ".join(guesses))
        score_percentage = round((score / len(self.questions)) * 100)
        print(f"Your score is: {score_percentage}%")


         


class OverallScore:
    def __init__(self):
        self.scores = {
            "GuessNumberGame": 0,
            "RockPaperScissors": 0,
            "TriviaPursuit": 0,
            "PokemonBinder": 0,
        }

    def add_score(self, game_name, points):
        if game_name in self.scores:
            self.scores[game_name] += points

    def get_score(self, game_name):
        return self.scores.get(game_name, 0)

    def display_scores(self):
        print("\n=== Overall Scores ===")
        for game, score in self.scores.items():
            print(f"{game}: {score}")


class PokemonBinder:
    """A simple class to manage a Pokemon card binder."""

    def __init__(self):
        """
        Initialize a new Pokemon binder.
        - self.cards keeps track of collected Pokemon Pokedex numbers (unique, no duplicates).
        - self.max_pokedex is the maximum Pokedex number allowed.
        - self.card_details stores where each card is placed: page, row, column, name, type, and rarity.
        - self.positions_per_page is how many cards fit on a single page (8 rows × 8 columns = 64).
        """
        self.cards = set()  # Use a set to avoid duplicates easily
        self.max_pokedex = 1025
        self.card_details = {}
        self.positions_per_page = 64  # Each page has 64 slots (8x8 grid)

    def calculate_placement(self, pokedex_num):
        """
        Determine where to place a new card in the binder.
        - pokedex_num is the Pokedex number of the card.
        Returns a tuple: (page, row, column)
        """
        total_cards = len(self.cards) + 1  # Include the new card
        page = (total_cards - 1) // self.positions_per_page + 1  # Calculate page number
        position_in_page = (total_cards - 1) % self.positions_per_page  # Position on the page (0 to 63)
        row = position_in_page // 8 + 1  # Calculate row (1 to 8)
        column = position_in_page % 8 + 1  # Calculate column (1 to 8)
        return page, row, column

    def add_card(self, pokedex_num, name, card_type, rarity):
        """
        Try to add a Pokemon card based on its Pokedex number and additional attributes.
        - Checks that the number is valid and not already added.
        - Calculates placement if successful.
        - Returns placement details or None if failed.
        """
        try:
            pokedex_num = int(pokedex_num)
            if pokedex_num < 1 or pokedex_num > self.max_pokedex:
                print(f"Invalid! Please enter a number between 1 and {self.max_pokedex}.")
                return None
            if pokedex_num in self.cards:
                print(f"Pokedex #{pokedex_num} is already in your binder.")
                return None
            page, row, column = self.calculate_placement(pokedex_num)
            self.cards.add(pokedex_num)
            self.card_details[pokedex_num] = {
                'name': name,
                'type': card_type,
                'rarity': rarity,
                'page': page,
                'row': row,
                'column': column
            }
            return {'page': page, 'row': row, 'column': column, 'pokedex_num': pokedex_num, 'name': name, 'type': card_type, 'rarity': rarity}
        except ValueError:
            print("That is not a valid number. Please try again.")
            return None

    def reset_binder(self):
        """Empty the binder by removing all cards."""
        self.cards.clear()
        self.card_details.clear()
        print("Your binder has been reset and is now empty.")

    def view_placements(self):
        """Display where each collected Pokemon card is placed along with details."""
        if not self.cards:
            print("Your binder is empty.")
            return
        print("\nCurrent Binder Cards:")
        print("-" * 50)
        for num in sorted(self.cards):
            place = self.card_details[num]
            print(f"Pokedex #{num}: {place['name']} (Type: {place['type']}, Rarity: {place['rarity']})")
            print(f"  - Page: {place['page']}, Row: {place['row']}, Column: {place['column']}")
        print("-" * 50)
        print(f"Total cards collected: {len(self.cards)}")
        percent = (len(self.cards) / self.max_pokedex) * 100
        print(f"Completion: {percent:.2f}%")
        if len(self.cards) == self.max_pokedex:
            print(" Congratulations! You have caught them all! ")

    def run_binder_manager(self):
        """Run the interactive menu to manage the binder."""
        print("\n=== Welcome to the Pokemon Card Binder Manager ===")
        while True:
            print("\nMenu:")
            print("1. Add a Pokemon card")
            print("2. Reset binder")
            print("3. View current cards")
            print("4. Exit program")
            choice = input("Choose an option (1-4): ")
            if choice == "1":
                pokedex_num = input("Enter the Pokedex number of the card: ")
                name = input("Enter the name of the card: ")
                card_type = input("Enter the type of the card: ")
                rarity = input("Enter the rarity of the card: ")
                result = self.add_card(pokedex_num, name, card_type, rarity)
                if result:
                    print(f"\nAdded {result['name']} (Pokedex #{result['pokedex_num']}) at:")
                    print(f" Page {result['page']}, Row {result['row']}, Column {result['column']}")
            elif choice == "2":
                confirm = input("Are you sure you want to reset the binder? Type YES to confirm: ")
                if confirm.strip().upper() == "YES":
                    self.reset_binder()
                else:
                    print("Reset cancelled.")
            elif choice == "3":
                self.view_placements()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please enter a number between 1 and 4.")



def main_menu():
    overall_score = OverallScore()

    while True:
        print("\n=== Game Menu ===")
        print("1. Guess the Number Game")
        print("2. Rock, Paper, Scissors")
        print("3. Trivia Pursuit")
        print("4. Pokemon Card Binder Manager")
        print("5. View Overall Scores")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            game = GuessNumberGame()
            won = game.play()
            if won:
                overall_score.add_score("GuessNumberGame", 10)
        elif choice == "2":
            game = RockPaperScissors()
            wins = game.play()
            if wins:
                overall_score.add_score("RockPaperScissors", wins)
        elif choice == "3":
            game = TriviaPursuit()
            game.play()
            # Add fixed points or extend to add scoring
            overall_score.add_score("TriviaPursuit", 5)
        elif choice == "4": 
            game =PokemonBinder()
            game.run_binder_manager()
        elif choice == "5":
            overall_score.display_scores()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 6.")
        


main_menu()
 
         
      




            




    
    
    


   











            




    
    
    


   






