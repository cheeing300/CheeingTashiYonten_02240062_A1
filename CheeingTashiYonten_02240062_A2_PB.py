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
            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                pokedex_num = input("Enter the Pokedex number of the card: ").strip()
                name = input("Enter the name of the card: ").strip()
                card_type = input("Enter the type of the card: ").strip()
                rarity = input("Enter the rarity of the card: ").strip()
                result = self.add_card(pokedex_num, name, card_type, rarity)
                if result:
                    print(f"\nAdded {result['name']} (Pokedex #{result['pokedex_num']}) at:")
                    print(f" Page {result['page']}, Row {result['row']}, Column {result['column']}")
            elif choice == "2":
                confirm = input("Are you sure you want to reset the binder? Type YES to confirm: ").strip()
                if confirm.upper() == "YES":
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


    binder = PokemonBinder()
    binder.run_binder_manager()
