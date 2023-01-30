import random

class Card():
    RANKS = (2,3,4,5,6,7,8,9,10,11,12,13,14)
    SUITS = ('C','D','H','S')

    # constructor
    def __init__(self, rank=12, suit= 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string rapresentation of a Card object
    def __str__(self):
        if self.rank == '14':
            rank = 'A'
        elif self.rank == 12:
            rank = 'K'
        elif self.rank == 11:
            rank = 'Q'
        elif self.rank == 10:
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit

    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank
    
    def __lt_(self, other):
        return self.rank < other.rank
    
    def __le__(self, other):
        return self.rank <= other.rank
    
    def __he__(self, other):
        return self.rank >= other.rank
    
    def __gt__(self, other):
        return self.rank > other.rank

class Deck():
    # constructor
    def __init__(self, num_decks = 1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card (rank, suit)
                    self.deck.append(card)
    
    # shuffle
    def shuffle(self):
        random.shuffle(self.deck)

    def deal (self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)
    
class Poker ():
    def __init__(self,  num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards
        
        # deal all the cards
        for i in range(num_players):
            hand = [] 
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.all_hands.apppend(hand)
        
    def play(self):
        # sort the hands of each player and print
        for i in range (len(self.all_hands)):
            sorted_hand = sorted(self.all_hands[i], reverse=True)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player: ' + str(i + 1) + ': ' + hand_str)