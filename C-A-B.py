import random

class CardsAgainstBoredom:

    def __init__(self):

        self.black_cards = [

            "Why did the chicken cross the road?",
            "What's that smell?",
            "What's my secret power?",
            "What never fails to liven up the party?",
            "What's the next superhero superpower?",
            "What's the best cure for a Sea-sickness?",
            "What's the next big reality TV show?",
            "What did I bring to the birthday Party?",
            "What's the newest Law passed?",
            "What's the key to a successful relationship?",
            "What's my guilty pleasure?",
            "What's the worst advice?",
            "What's my spirit animal?",
            "What will I bring back in time to impress people?",
            "What's the meaning of life?",
            "What's the ultimate weapon to fight zombies?",
            "What's the secret to happiness?",
            "What's the next viral sensation?",
            "What's the worst thing to say in a job interview?",
            "What's the best way to spend a Friday night?"

        ]
        self.white_cards = [

            "Blaming it on the dog",
            "Dancing like no one is watching",
            "Eating too much candy",
            "Wearing socks with sandals",
            "Running through a sprinkler",
            "Making a mixtape",
            "Using 'Google' as a verb",
            "Catching a cold",
            "Binge-watching Netflix",
            "Playing air guitar",
            "Finding money in your pocket",
            "Having an existential crisis",
            "Spilling coffee on yourself",
            "Reading the last page of the book first",
            "Forgetting someone's name",
            "Talking to plants",
            "Singing karaoke alone",
            "Daydreaming in class",
            "Getting lost in a foreign country",
            "Making a midnight snack"
            
        ]

        self.players = []

        self.current_player_index = 0

    def add_player(self, name):

        if len(self.players) < 6:

            self.players.append(name)

        else:

            print("Maximum number of players is 6.")

    def draw_black_card(self):

        return random.choice(self.black_cards)

    def draw_white_cards(self, num_cards=1):

        return random.sample(self.white_cards, num_cards)

    def choose_winner(self):

        print("Choose the winning player:")

        for i, player in enumerate(self.players):

            print(f"{i+1}. {player}")

        while True:

            try:
                winner_index = int(input("Enter the number of the winning player: ")) - 1

                if 0 <= winner_index < len(self.players):

                    return winner_index

                else:

                    print("Invalid player number. Please choose again.")

            except ValueError:

                print("Invalid input. Please enter a number.")

    def play_round(self):

        print("Current black card: ", self.draw_black_card())

        print("")

        for i, player in enumerate(self.players):

            print(f"Player {i+1} ({player}), it's your turn.")

            input("Press Enter to draw your white card.")

            print("Your white card: ", self.draw_white_cards())

            print("")
        winner_index = self.choose_winner()

        print(f"Player {winner_index+1} ({self.players[winner_index]}) wins this round!")

        print("")

    def start_game(self):

        print("Welcome to Cards Against Boredom!")

        print("")

        num_players = int(input("Enter the number of players (Max6): "))

        for i in range(num_players):

            player_name = input(f"Enter the name of Player {i+1}: ")

            self.add_player(player_name)

        while True:

            self.play_round()

            continue_game = input("Do you want to continue playing? (yes/no): ")

            if continue_game.lower() != 'yes':

                print("Thanks for playing!")

                break

if __name__ == "__main__":

    game = CardsAgainstBoredom()

    game.start_game()
