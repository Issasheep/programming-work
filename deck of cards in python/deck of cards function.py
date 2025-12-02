money = 100000
bet = 0

full_deck = []

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit} (Value: {self.value})"

class face_card:
    def __init__(self):
        self.suit = 'Face Cards'
        self.value = 10
        self.values = {'Jack', 'Queen', 'King'}
    def __str__(self):
        return f"{self.suit}: {self.values}"

class suits: 
    def __init__(self, cards):
        self.cards = cards
        self.suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']



def get_cards(self):
    return self.cards



def deck_of_cards():
    deck = []
    suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
    ranks_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
    }

    for suit in suits:
        for rank, value in ranks_values.items():
            deck.append(Card(suit, rank, value))
    
    return deck



def shuffle_deck(deck_of_cards):
    import random
    random.shuffle(deck_of_cards)
    return deck_of_cards

deckes = shuffle_deck(deck_of_cards())
for i in range (52):
    print (deckes[0].value)



"""
#full_deck = shuffle_deck(deck_of_cards())
#full_deck = shuffle_deck(deck_of_cards())

#print (full_deck, "\n")
#black_jack_game()

player_score = 0
dealer_score = 0

full_deck = shuffle_deck(deck_of_cards())

if len(full_deck) <= 5:
    print("Not enough cards to continue the game.")
    full_deck = shuffle_deck(deck_of_cards())

player_inventory = [full_deck[0], full_deck[1]]
full_deck.pop(0)
full_deck.pop(0)

dealer_inventory = [full_deck[0], full_deck[1]]
full_deck.pop(0)
full_deck.pop(0)

player_inventory += [full_deck[2], full_deck[3]]
full_deck.pop(0)
full_deck.pop(0)

print("Player's Cards: ", player_inventory[0], ", ", player_inventory[1], player_inventory[0], ", ", player_inventory[1])
print("Dealer's Cards: ", dealer_inventory[0], ", ", "Hidden Card \n",)

player_score = player_inventory[0].value + player_inventory[1].value

while True or player_score < 21:


    player_input = input("Type 'y' to get another card, type 'n' to pass: ") 

    if player_input == 'y':
        player_card_3 = full_deck[0]
        full_deck.pop[0]
        print("Player's Cards: ", player_inventory[0], ", ", player_inventory[1], ", ", player_card_3)

    else:
        print("Player stands with: ", player_inventory[0], ", ", player_inventory[1])


    player_score = player_inventory[0].value + player_inventory[1].value + player_card_3.value

    
    """