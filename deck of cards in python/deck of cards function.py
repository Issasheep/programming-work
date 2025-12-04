import time
while True:
    player_inventory = []
    dealer_inventory = []


    money = 100000
    bet = 0

    full_deck = []



    class Card:
        def __init__(self, suit, rank, value):
            self.suit = suit
            self.rank = rank
            self.value = value

        def __str__(self):
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
    
    def ace_checker():
        if player_inventory[0].rank == 'Ace' and player_inventory[1].rank == 'Ace':
            player_inventory[0].value = 11
            player_inventory[1].value = 1
        if dealer_inventory[0].rank == 'Ace' and dealer_inventory[1].rank == 'Ace':
            dealer_inventory[0].value = 11
            dealer_inventory[1].value = 1
    


    player_score = 0
    dealer_score = 0

    full_deck = shuffle_deck(deck_of_cards())

    if len(full_deck) <= 5:
        print("Not enough cards to continue the game.")
        full_deck = shuffle_deck(deck_of_cards())

    def player_append_card():
        player_inventory.append(full_deck[0])
        full_deck.pop(0)
    

    def dealer_append_card():
        dealer_inventory.append(full_deck[0])
        full_deck.pop(0)

    for i in range(2):
        player_append_card()
        dealer_append_card()

    #print("Player's Cards: ", player_inventory[0], ", ", player_inventory[1]  ,"total value: ", player_inventory[0].value + player_inventory[1].value)
    print (player_inventory)
    print (dealer_inventory)
    print("Dealer's Cards: ", dealer_inventory[0], ", ", "Hidden Card \n",)
    ace_checker()
    player_score = player_inventory[0].value + player_inventory[1].value

    while player_score <= 22 or player_input == 'n':


        player_input = input("Type 'y' to get another card, type 'n' to pass: ")
        player_input = player_input.lower()

        if player_input == 'y':
            player_card_3 = full_deck[0]
            full_deck.pop(0)
            print("Player's Cards: ", player_inventory[0], ", ", player_inventory[1], ", ", player_card_3)
            print("Dealer's Cards: ", dealer_inventory[0], ", ", "Hidden Card \n",)

            if player_inventory[0].value + player_inventory[1].value + player_card_3.value > 21:
                print("Player busts! Total value: ", player_inventory[0].value + player_inventory[1].value + player_card_3.value)
                time.sleep (1)
                break

            else:
                player_score = player_inventory[0].value + player_inventory[1].value + player_card_3.value
                break
        else:
            print("Player's Cards: ", player_inventory[0], ", ", player_inventory[1]  ,"total value: ", player_inventory[0].value + player_inventory[1].value)

            print("Dealer's Cards: ", dealer_inventory[0], ", ", dealer_inventory[1])
            dealer_score = dealer_inventory[0].value + dealer_inventory[1].value

            if dealer_score < 17:
                dealer_card_3 = full_deck[0]
                full_deck.pop(0)

                print("Dealer's Cards: ", dealer_inventory[0], ", ", dealer_inventory[1], ", ", dealer_card_3)
                dealer_score = dealer_inventory[0].value + dealer_inventory[1].value + dealer_card_3.value

                if dealer_score > 21:
                    print("Dealer busts! Total value: ", dealer_score)
                    time.sleep (1)
                
