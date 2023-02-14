#  File: Poker.py

#  Description: This program simulates a regular Poker game, otherwise known as the 5-Card Draw.

#  Student's Name: Julian Canales

#  Student's UT EID: jac22779

#  Partner's Name: Simaak Siddiqi

#  Partner's UT EID: srs5826

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 2/13/2023

#  Date Last Modified: 2/13/2023

import sys, random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.players_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.players_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)
      self.players_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ': ' + hand_str)
    
    print()

    # determine the type of each hand and print
    hand_type = []	# create a list to store type of hand
    hand_points = []	# create a list to store points for hand
    
    
    for i in range(len(self.players_hands)):
      if self.is_royal(self.players_hands[i])[0]:
        hand_type.append(self.is_royal(self.players_hands[i])[1])
        hand_points.append(self.is_royal(self.players_hands[i])[0])
      elif self.is_straight_flush(self.players_hands[i])[0]:
        hand_type.append(self.is_straight_flush(self.players_hands[i])[1])
        hand_points.append(self.is_straight_flush(self.players_hands[i])[0])
      elif self.is_four_kind(self.players_hands[i])[0]:
        hand_type.append(self.is_four_kind(self.players_hands[i])[1])
        hand_points.append(self.is_four_kind(self.players_hands[i])[0])
      elif self.is_full_house(self.players_hands[i])[0]:
        hand_type.append(self.is_full_house(self.players_hands[i])[1])
        hand_points.append(self.is_full_house(self.players_hands[i])[0])
      elif self.is_flush(self.players_hands[i])[0]:
        hand_type.append(self.is_flush(self.players_hands[i])[1])
        hand_points.append(self.is_flush(self.players_hands[i])[0])
      elif self.is_straight(self.players_hands[i])[0]:
        hand_type.append(self.is_straight(self.players_hands[i])[1])
        hand_points.append(self.is_straight(self.players_hands[i])[0])
      elif self.is_three_kind(self.players_hands[i])[0]:
        hand_type.append(self.is_three_kind(self.players_hands[i])[1])
        hand_points.append(self.is_three_kind(self.players_hands[i])[0])
      elif self.is_two_pair(self.players_hands[i])[0]:
        hand_type.append(self.is_two_pair(self.players_hands[i])[1])
        hand_points.append(self.is_two_pair(self.players_hands[i])[0])
      elif self.is_one_pair(self.players_hands[i])[0]:
        hand_type.append(self.is_one_pair(self.players_hands[i])[1])
        hand_points.append(self.is_one_pair(self.players_hands[i])[0])
      else:
        hand_type.append(self.is_high_card(self.players_hands[i])[1])
        hand_points.append(self.is_high_card(self.players_hands[i])[0])
      print(f'Player {i+1}: {hand_type[i]}')

  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    points_alloted = 10
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    points = points_alloted * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'

  def is_straight_flush (self, hand):
    points_alloted = 9
    same_suit = True
    for i in range(len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''
    
    rank_order = True
    high_card_rank = hand[0].rank
    for i in range(len(hand)):
      rank_order = rank_order and (hand[i].rank == high_card_rank - i)
    
    if (not rank_order):
      return 0, ''
    
    points = points_alloted * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight Flush'

  def is_four_kind (self, hand):
    # the four of a kind can only occur in the first 4 cards or last 4 cards
    points_alloted = 8
    start_count = 0
    if hand[0].rank != hand[1].rank:
      start_count = 1

    same_rank = True
    for i in range(start_count, start_count + 4 - 1):
      same_rank = same_rank and (hand[i].rank == hand[i+1].rank)

    if (not same_rank):
      return 0, ''
    
    if start_count == 0:
      points = points_alloted * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)
    
    if start_count == 1:
      points = points_alloted * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
      points = points + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1
      points = points + (hand[0].rank)

    return points, 'Four of a Kind'


  def is_full_house (self, hand):
    points_alloted = 7

    start_count_triple = 2
    start_count_double = 0
    if hand[2].rank != hand[3].rank:
      start_count_triple = 0
      start_count_double = 3

    same_rank_triple = True
    for i in range(start_count_triple, start_count_triple + 2):
      same_rank_triple = same_rank_triple and (hand[i].rank == hand[i+1].rank)

    same_rank_double = True
    for i in range(start_count_double, start_count_double + 1):
      same_rank_double = same_rank_double and (hand[i].rank == hand[i+1].rank)
    
    if (not same_rank_double) or (not same_rank_triple):
      return 0, ''
    
    if start_count_triple == 0:
      points = points_alloted * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

    if start_count_triple == 2:
      points = points_alloted * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
      points = points + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
      points = points + (hand[1].rank)

    return points, 'Full House'

  def is_flush (self, hand):
    points_alloted = 6

    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''
    
    points = points_alloted * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    
    return points, 'Flush'


  def is_straight (self, hand):
    points_alloted = 5

    rank_order = True
    high_card_rank = hand[0].rank
    for i in range(len(hand)):
      rank_order = rank_order and (hand[i].rank == high_card_rank - i)
    
    if (not rank_order):
      return 0, ''
    
    points = points_alloted * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight'

  def is_three_kind (self, hand):
    points_alloted = 4

    start_count = 0

    if hand[0].rank != hand[1].rank:
      start_count = 1

    if hand[1].rank != hand[2].rank:
      start_count = 2

    same_rank = True
    for i in range(start_count, start_count + 2):
      same_rank = same_rank and (hand[i].rank == hand[i+1].rank)
    
    if (not same_rank):
      return 0, ''
    if start_count == 0:
      points = points_alloted * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
      points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
      points = points + (hand[4].rank)

    if start_count == 1:
      points = points_alloted * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3
      points = points + (hand[3].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
      points = points + (hand[4].rank)

    if start_count == 2:
      points = points_alloted * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3
      points = points + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1
      points = points + (hand[1].rank)

    return points, 'Three of a Kind'

  def is_two_pair (self, hand):
    points_alloted = 3
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        k = i
        break
    
    two_pair = False
    if one_pair: 
      for i in range(k + 2, len(hand)-1):
        if (hand[i].rank == hand[i + 1].rank):
          two_pair = True
          j = i
          break

    if one_pair and two_pair:
      if hand[k].rank > hand[j].rank:
        one_pair_higher_ranking = True
      
      else:
        one_pair_higher_ranking = False

      if one_pair_higher_ranking:
        if j-k > 2 and k == 0:
          points = points_alloted * 15 ** 5 + (hand[k].rank) * 15 ** 4 + (hand[k+1].rank) * 15 ** 3
          points = points + (hand[j].rank) * 15 ** 2 + (hand[j+1].rank) * 15 ** 1
          points = points + (hand[2].rank)
        elif j-k == 2 and k ==0:
          points = points_alloted * 15 ** 5 + (hand[k].rank) * 15 ** 4 + (hand[k+1].rank) * 15 ** 3
          points = points + (hand[j].rank) * 15 ** 2 + (hand[j+1].rank) * 15 ** 1
          points = points + (hand[4].rank)
        else:
          points = points_alloted * 15 ** 5 + (hand[k].rank) * 15 ** 4 + (hand[k+1].rank) * 15 ** 3
          points = points + (hand[j].rank) * 15 ** 2 + (hand[j+1].rank) * 15 ** 1
          points = points + (hand[0].rank)
      
      if (not one_pair_higher_ranking):
        if j-k > 2 and k == 0:
          points = points_alloted * 15 ** 5 + (hand[j].rank) * 15 ** 4 + (hand[j+1].rank) * 15 ** 3
          points = points + (hand[k].rank) * 15 ** 2 + (hand[k+1].rank) * 15 ** 1
          points = points + (hand[2].rank)
        elif j-k == 2 and k ==0:
          points = points_alloted * 15 ** 5 + (hand[j].rank) * 15 ** 4 + (hand[j+1].rank) * 15 ** 3
          points = points + (hand[k].rank) * 15 ** 2 + (hand[k+1].rank) * 15 ** 1
          points = points + (hand[4].rank)
        else:
          points = points_alloted * 15 ** 5 + (hand[j].rank) * 15 ** 4 + (hand[j+1].rank) * 15 ** 3
          points = points + (hand[k].rank) * 15 ** 2 + (hand[k+1].rank) * 15 ** 1
          points = points + (hand[0].rank)


      return points, 'Two Pair'
    
    else:
      return 0, ''

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_one_pair (self, hand):
    points_alloted = 2
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        k = i
        break
    if (not one_pair):
      return 0, ''
    
    listOfCardsNotInOnePair = []
    for i in range(2,5):
      listOfCardsNotInOnePair.append(hand[(k+i) % 5].rank)

    listOfCardsNotInOnePair.sort(reverse=True)

    points = points_alloted * 15 ** 5 + (hand[k].rank) * 15 ** 4 + (hand[k+1].rank) * 15 ** 3
    points = points + listOfCardsNotInOnePair[0] * 15 ** 2 + listOfCardsNotInOnePair[1] * 15 ** 1
    points = points + listOfCardsNotInOnePair[2]

    return points, 'One Pair'

  def is_high_card (self,hand):
    points_alloted = 1

    points = points_alloted * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
    
    return points, 'High Card'

def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()

