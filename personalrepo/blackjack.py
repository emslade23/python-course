import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        print('{} of {}').format(self.rank, self.suit)


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        #cards = ''  # start with an empty string
        for card in self.deck:
            card.__str__()  # add each Card object's print string
        #return 'The deck has: \n' + cards

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value = self.value + values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value = self.value - 10
            self.aces = self.aces - 1


class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(raw_input("Pick your bet (must be integer value): "))
        except ValueError:
            print('Sorry a bet must be an integer value')
        else:
            if chips.bet > chips.total:
                print('Your bet cannot exceed your total amount:', chips.total)
            else:
                break

def hit(deck,hand):
    print("BLAAA")
    deck.__str__()
    deal = deck.deal()
    hand.add_card(deal)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing #global variable
    while True:
        playerschoice = raw_input('Hit or Stand? Enter "Hit" or "Stand": ')
        if playerschoice == 'Hit':
            hit(deck, hand)
            break
        elif playerschoice == 'Stand':
            print("Player stands. Dealer is playing.")
            playing = False
            break
        else:
            print("Please try again")
            continue
        
        

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden> ")
    dealer.cards[1].__str__()
    print("\n Player's Hand: ")
    for card in player.cards:
        card.__str__()
    


def show_all(player, dealer):
    print("\nDealer's Hand:")
    for dealercard in dealer.cards:
        dealercard.__str__()
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:")
    for card in player.cards:
        card.__str__()
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


while True:
    # Print an opening statement
    print("Welcome to Python BlackJack!")
    # Create & shuffle the deck, deal two cards to each player
    
    deck = Deck()
    deck.shuffle()
    deck.__str__()
    playerhand = Hand()
    playerhand.add_card(deck.deal())
    playerhand.add_card(deck.deal())
    
    dealerhand = Hand()
    dealerhand.add_card(deck.deal())
    dealerhand.add_card(deck.deal())
    
        
    # Set up the Player's chips
    playerchips = Chips()
    
    # Prompt the Player for their bet
    take_bet(playerchips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(playerhand, dealerhand)

    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, playerhand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(playerhand, dealerhand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if playerhand.value > 21:
            player_busts(playerhand, dealerhand, playerchips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if playerhand.value <= 21:
        while dealerhand.value < 17:
            hit(deck, dealerhand)
    
        # Show all cards
        show_all(playerhand, dealerhand)
        
        # Run different winning scenarios
        if dealerhand.value > playerhand.value:
            dealer_busts(playerhand, dealerhand, playerchips)
            
        elif dealerhand.value > playerhand.value:
            dealer_wins(playerhand, dealerhand, playerchips)
            
        else:
            push(playerhand, dealerhand)
    
    # Inform Player of their chips total 
    print("Player's winnings are ", playerchips.total)
    # Ask to play again
    playagain = raw_input("Would you like to play again? Enter y or n: ")
    if playagain[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing!')
        break