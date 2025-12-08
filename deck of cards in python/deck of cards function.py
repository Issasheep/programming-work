import time

player_inventory = []
dealer_inventory = []

player_score = 0
dealer_score = 0

bet = 0
player_bet = 0
money = 100000

full_deck = []

def ace_checker():
    if player_inventory[0].rank == 'Ace' and player_inventory[1].rank == 'Ace':
        player_inventory[0].value = 11
        player_inventory[1].value = 1
    if dealer_inventory[0].rank == 'Ace' and dealer_inventory[1].rank == 'Ace':
        dealer_inventory[0].value = 11
        dealer_inventory[1].value = 1

def player_append_card():
    player_inventory.append(full_deck[0])
    full_deck.pop(0)


def dealer_append_card():
    dealer_inventory.append(full_deck[0])
    full_deck.pop(0)

def dealing_cards():

    for i in range(2):
        player_append_card()
        dealer_append_card()

    print ("\n Dealing Cards... \n")
    print ("------------------\n")
    print ("player's cards: ", end="")

    for i in range(len(player_inventory)):
        print (player_inventory[i], end=", ")
    print (f"total value: {player_inventory[0].value + player_inventory[1].value}\n")

    print ("dealer's cards: ",dealer_inventory[1],"dealer's total value is hidden\n")
    print ("\n------------------\n")

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class face_card:
    def __init__(self):
        self.suit = 'Face Cards'
        self.value = 10
        self.values = {'Jack', 'Queen', 'King'}
    def __str__(self):
        return f"{self.suit}: {self.values} "



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

while True:

    full_deck = shuffle_deck(deck_of_cards())
    print ("Welcome to Blackjack!\n")
    print("You have $", money)
    bet = input("how much would you like to bet?: ")
    money -= int(bet)

    if len(full_deck) <= 5:
        print("Not enough cards to continue the game.")
        full_deck = shuffle_deck(deck_of_cards())

    dealing_cards()
    time.sleep (1)
    ace_checker()
    for i in range(len(player_inventory)):
        player_score += player_inventory[i].value

    while player_score <= 22 or player_input == 'n':


        player_input = input("Type 'y' to get another card, type 'n' to pass: ")
        player_input = player_input.lower()
        while player_input != 'y' and player_input != 'n':
            player_append_card()
            print ("------------------\n")
            print ("player's cards: ", end="")

            for i in range(len(player_inventory)):
                print (player_inventory[i], end=", ")

            for i in range(len(player_inventory)):
                player_score += player_inventory[i].value

            print("Dealer's Cards: ", dealer_inventory[0], ", ", "Hidden Card \n",)

            if player_score > 21:
                print("Player busts! Total value: ", player_score)
                time.sleep (1)
                break

            else:
                for i in range(len(player_inventory)):
                    player_score += player_inventory[i].value
                break

        dealer_score = dealer_inventory[0].value + dealer_inventory[1].value
        while dealer_score < 17:
            dealer_card_3 = full_deck[0]
            full_deck.pop(0)

            for i in range(len(dealer_inventory)):
                dealer_score += dealer_inventory[i].value

            print("Dealer's Cards: ")
            for i in range(len(dealer_inventory)):
                print (dealer_inventory[i], end=", ")

            if dealer_score > 22:
                print("Dealer busts! Total value: ", dealer_score)
                time.sleep (1)
                break
            
        dealer_score = 21 - (dealer_inventory[0].value + dealer_inventory[1].value)
        player_score = 21 - (player_inventory[0].value + player_inventory[1].value)

        if dealer_score < player_score:
            print("Player wins!")
            player_bet = bet * 2
            time.sleep (1)
            break

        elif dealer_score < player_score:
            print("Dealer wins!")
            player_bet = 0
            time.sleep (1)
            break

        else:
            print("push!")
            player_bet = bet
            time.sleep (1)
            break

    money += player_bet
    print("Player's money: ", money)
    print ("\n------------------\n")
    if money <= 0:
        print("You are out of money! Game over.")
        break
    