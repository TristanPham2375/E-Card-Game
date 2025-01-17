"""
-------------------------------------------------------
Player and Card class
-------------------------------------------------------
Author:  Tristan Pham
Email:   haitrung2375@gmail.com
__updated__ = "2025-01-16"
-------------------------------------------------------
"""


class Card:

    def __init__(self, value):
        """
        Initializes a card with a role
        Use: card = Card(value)
        Parameters:
            value - one of the three classes of cards.
        """
        valid_values = ['emperor', 'slave', 'citizen']
        if value not in valid_values:
            raise ValueError(
                f"Invalid role '{value}'. Must be one of {valid_values}.")
        else:
            self._role = value

    def compare(self, target):
        """
        Compares self and target card to see which one is bigger
        Use: value = card.compare(target)
        Parameters:
            target - the object that is being compared to.
        Return: -1 if card is bigger, 0 if they are equal, 1 if target is bigger
        """
        i = 0
        if self._role == 'emperor':
            if target._role == 'citizen':
                i = -1
            elif target._role == 'slave':
                i = 1
        elif self._role == 'citizen':
            if target._role == 'emperor':
                i = 1
            elif target._role == 'slave':
                i = -1
            elif target._role == 'citizen':
                i = 0
        elif self._role == 'slave':
            if target._role == 'emperor':
                i = -1
            elif target._role == 'citizen':
                i = 1
        return i

    def string(self):
        """
        Returns a string representation of the card's role
        Use: card.string()
        """
        return self._role


class Player:

    def __init__(self):
        """
        Initializes a player hand
        The hand holds max 5 cards
        Use: player = Player()
        """
        self._hand = []
        self._length = 0

    def addcard(self, Card):
        """
        Adds a card to the player's hand, ensuring the hand doesn't exceed 5 cards
        Use: player.addcard(Card)
        Parameters:
            Card - a card object being added to the player's hand.
        """
        if len(self._hand) < 5:
            self._hand.append(Card)
        else:
            raise ValueError("Hand is full. You can't have more than 5 cards.")

        self._length += 1

    def display(self, ):
        """ 
        Displays the cards you have on hand
        Use: player.display()
        """
        if len(self._hand) > 0:
            print(f"Cards on hand: ")
            for i in range(0, len(self._hand), 1):
                card = self._hand[i]
                print(f"{i} - {card.string()}")
        else:
            print(f"No cards in hand")

    def play_card(self, index):
        """
        Allows the player to play a card by removing it from the hand
        Use: player.play_card(index)
        Parameters:
            index - the index of the card on the players hand (index starts from 0).
        """
        if len(self._hand) == 0:
            raise ValueError("No cards left to play")

        if index < 0 or index >= len(self._hand):
            raise ValueError("Invalid card index, please choose a valid index")

        played_card = self._hand[index]
        print(f"You played: {played_card.string()}")
        return played_card

    def play_card_bot(self, index):
        """
        Allows the bot to play a card by removing it from the hand
        Use: bot.play_card_bot(index)
        Parameters:
            index - the index of the card on the bot's hand (index starts from 0).
        """
        if len(self._hand) == 0:
            raise ValueError("No cards left to play")

        if index < 0 or index >= len(self._hand):
            raise ValueError("Invalid card index, please choose a valid index")

        played_card = self._hand[index]
        print(f"Bot played: {played_card.string()}")
        return played_card

    def is_empty(self):
        """
        Determines if player hand is empty
        Use: b = player.is_empty()
        """
        if len(self._hand) == 0:
            empty = True
        else:
            empty = False
        return empty

    def pop(self, index):
        """
        Remove card from player hand
        Use: player.pop(index)
        Parameters:
            index - the index of the card on the players hand (index starts from 0).
        """
        if index < 0 or index >= len(self._hand):
            raise ValueError("Invalid card index, please choose a valid index")
        else:
            self._hand.pop(index)
            self._length -= 1

    def __len__(self):
        """
        Returns the amount of cards left of players hand
        Use: len(player)
        """
        return self._length

    def has_emperor(self):
        """
        Checks if there is a 'emperor' in the player's hand
        Use: player.has_king()
        """
        for card in self._hand:
            if card._role == 'emperor':
                return True
        return False

    def has_slave(self):
        """
        Checks if there is a 'slave' in the player's hand
        Use: player.has_slave()
        """
        for card in self._hand:
            if card._role == 'slave':
                return True
        return False
