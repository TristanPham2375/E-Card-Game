# imports
from player_and_card_class import Card, Player
from random import randint

print("Welcome to Kaiji's death game")
print()
print("Rules:")
print("There are 2 deck of 5 cards each: one with a slave and 4 citizens - one with an emperor and 4 citizens")
print("Every turn, each player puts a card on the table, if the the cards are:")
print("citizen - citizen => draw")
print("citizen - slave => citizen wins and player 1 wins the game")
print("emperor - citizen => emperor wins")
print("emperor - slave => slave wins and player 2 wins the game")
print("Played cards are removed from the table after each turn")
print("Tip: Playing as slave will make the game a lot harder to win. If you wish to play as Kaiji, take the Slave's side")
print()

replay = 'Y'
# Start of game loop
while replay.upper() == 'Y':
    side = str(input("Choose the side you wish to play as (S/E): "))

    # Initialize players
    player = Player()
    player2 = Player()
    condition = True

    # Setup deck for player and player2 based on chosen side
    if side.upper() == 'E':  # Player chooses Emperor side
        player.addcard(Card("citizen"))
        player.addcard(Card("citizen"))
        player.addcard(Card("emperor"))
        player.addcard(Card("citizen"))
        player.addcard(Card("citizen"))

        player2.addcard(Card("citizen"))
        player2.addcard(Card("citizen"))
        player2.addcard(Card("slave"))
        player2.addcard(Card("citizen"))
        player2.addcard(Card("citizen"))

        turn = 1
        # Game loop for Emperor side
        while condition:
            player.display()  # Display the player's cards
            # Player chooses a card to play
            choose = int(input(f"Turn {turn}, choose a card number: "))
            print()
            a1 = player.play_card(choose)  # Play the selected card
            length = len(player2) - 1
            random = randint(0, length)  # Bot chooses a random card to play
            a2 = player2.play_card_bot(random)
            compare = a1.compare(a2)  # Compare cards

            if compare == -1:  # Player's card wins
                player2.pop(random)
                player.pop(choose)
                print(f"You won at round {turn}")
            elif compare == 0:  # Draw
                player2.pop(random)
                player.pop(choose)
                print(f"You draw round {turn}")
            elif compare == 1:  # Bot's card wins
                player.pop(choose)
                player2.pop(random)
                print(f"You lost at round {turn}")
            turn += 1
            print()

            # Check win/lose conditions based on cards remaining
            if player.has_emperor() == False and player2.has_slave() == False:
                condition = False
                print("You lost the game!")
            elif player2.has_slave() == False and player.has_emperor() == True:
                condition = False
                print("You won the game!")
            elif player2.has_slave() == True and player.has_emperor() == False:
                condition = False
                print("You won the game!")

    elif side.upper() == 'S':  # Player chooses Slave side
        player.addcard(Card("citizen"))
        player.addcard(Card("citizen"))
        player.addcard(Card("slave"))
        player.addcard(Card("citizen"))
        player.addcard(Card("citizen"))

        player2.addcard(Card("citizen"))
        player2.addcard(Card("citizen"))
        player2.addcard(Card("emperor"))
        player2.addcard(Card("citizen"))
        player2.addcard(Card("citizen"))

        turn = 1
        # Game loop for Slave side
        while condition:
            player.display()  # Display the player's cards
            # Player chooses a card to play
            choose = int(input(f"Turn {turn}, choose a card number: "))
            print()
            a1 = player.play_card(choose)  # Play the selected card
            length = len(player2) - 1
            random = randint(0, length)  # Bot chooses a random card to play
            a2 = player2.play_card_bot(random)
            compare = a1.compare(a2)  # Compare cards

            if compare == -1:  # Player's card wins
                player2.pop(random)
                player.pop(choose)
                print(f"You won at round {turn}")
            elif compare == 0:  # Draw
                player.pop(choose)
                player2.pop(random)
                print(f"You draw round {turn}")
            elif compare == 1:  # Bot's card wins
                player.pop(choose)
                player2.pop(random)
                print(f"You lost at round {turn}")
            turn += 1
            print()

            # Check win/lose conditions based on cards remaining
            if player2.has_emperor() == False and player.has_slave() == False:
                condition = False
                print("You won the game!")
            elif player.has_slave() == False and player2.has_emperor() == True:
                condition = False
                print("You lost the game!")
            elif player.has_slave() == True and player2.has_emperor() == False:
                condition = False
                print("You lost the game!")

    # Prompt user if they want to replay
    replay = str(input("Do you want to start a new game? (Y/N): "))
