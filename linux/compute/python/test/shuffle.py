import random

def create_deck():
    """ Create a standard deck of cards """
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    return [f'{value} of {suit}' for suit in suits for value in values]

def shuffle_deck(deck):
    """ Shuffle the deck of cards """
    random.shuffle(deck)

def main():
    deck = create_deck()
    print("Original deck:")
    print(deck)

    shuffle_deck(deck)
    print("\nShuffled deck:")
    print(deck)

if __name__ == "__main__":
    main()
