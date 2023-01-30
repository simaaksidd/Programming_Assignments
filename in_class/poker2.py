import random
import matplotlib.pyplot as plt
#Literal constants
SUITS = ['Heart', 'Club', 'Diamond', 'Spade']
FACECARDS = ['Ace', 'Jack', 'Queen', 'King']

#Just to verify that I'm not making a mistake in the code. Ideally, If a GUI is made for this, It won't be necessary to the user.
def isRank(r):
    return r == 'Ace' or r == '2' or r == '3' or r == '4' or r == '5' or r == '6' or r == '7' or r == '8' or r == '9' or r == '10' or r == 'Jack' or r == 'Queen' or r == 'King'
def isSuit(s):
    return s == "Diamond" or s == 'Spade' or s == 'Heart' or s == 'Club'


class Card():
    # Create a card class which has attributes "Rank" and "Suit"
    def __init__(self, rank, suit):
        if not isSuit(suit) or not isRank(rank): 
            print("Not a legal card")
            return   
        self.__rank = rank
        self.__suit = suit

# This is just important so python prints the string representation of the cards and not something like <object at 023503198ilsdafjaueuq03> 
    def __str__(self):
        return str(self.__rank) + " of " + str(self.__suit) + "s"
    def __repr__(self):
        return str(self)

    def getRank(self):
        return self.__rank

    def getSuit(self):
        return self.__suit

# Auxillary funcitons
def isPair(card1, card2):
    #Checks if a given 2 cards is a pair 
    if card1.getRank() == card2.getRank():
        return True
    return False

def checkForPairs(hand):
    '''
    Checks for pairs in a hand. This function only returns a 1 if there is a pair in the hand
    it does not return a 2 if there are 2 pairs in the hand because we are only looking at the 
    probablility that there is a pair, and if you get a two pair you still technically have a pair. 
    '''
    count = 0
    pair = []
    for i in range(1,5):
        if isPair(hand[0], hand[i]):
            pair.append((hand[0], hand[i]))
            count += 1
    for i in range(2,5):
        if isPair(hand[1], hand[i]):
            pair.append((hand[1], hand[i]))
            count += 1
    for i in range(3,5):
        if isPair(hand[2], hand[i]):
            pair.append((hand[2], hand[i]))
            count += 1
    if isPair(hand[3], hand[4]):
        pair.append((hand[3], hand[4]))
        count += 1
    if count >= 1:
        count = 1
    return pair, count

def shuffleAndDraw():
    #Creates a deck, shuffles the cards, and draws a 5 card hand. (I know this is usually not how poker works but lets just say it does for simplicities sake)
    deck = []
    hand = []
    for i in range(2, 11):
        for suit in SUITS:
            deck.append(Card(str(i), suit))
    for faceCard in FACECARDS:
        for suit in SUITS:
            deck.append(Card(faceCard, suit))
    random.shuffle(deck)
    for i in range(5):
        x = deck.pop()
        hand.append(x)
    return hand

def plotData(frequency, trials):
    #Plots the trial data on a handy graph
    y = frequency
    x = [i for i in range(1,trials+1)]
    
    plt.plot(x, y)

    plt.ylabel('Relative Frequency of Pairs')
    plt.xlabel('Number of Trials') 
    plt.title('Law of Large Numbers for probability of a Pair')

    plt.show()

#Driver function
def main():
    numberOfPairs = 0
    pairTurns = []
    relativeFrequency = []
    n = int(input("Enter a number of trials: "))
    for i in range(1,n+1):
        hand = shuffleAndDraw()
        numberOfPairs += int(checkForPairs(hand)[1])
        relativeFrequency.append(round((numberOfPairs / i), 3))
        if n <= 50:
            print("My hand is " + str(hand))
            print("")
            if checkForPairs(hand)[0] == []:
                print("0 Pairs")
                print("")
            else:
                pairTurns.append((i+1))
                print(str(checkForPairs(hand)[1]) + " pair(s): " + str(checkForPairs(hand)[0]))
                print("")
    
    # float division is weird in python so It might mess up the values, so I just put a round function to not mess anyhting up
    print("There were " + str(numberOfPairs) + " pairs in " + str(n) + " turns.")
    print("Relative frequency: " + str(relativeFrequency[n-1]))
    if n <= 50:
        print("The turns which the pairs were found were " + str(pairTurns))
    
    plotData(relativeFrequency, n)

main()