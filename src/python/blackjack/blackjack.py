from random import shuffle

values = {'1':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

def playAHand(deck,players):
    shuffle(deck)
    playerHand = {}
    outcome = {}
    ## Deal Cards
    dealerHand = dealHand(deck,2)
    dealerShowing = values[dealerHand[0][0]]
    for i in range(players):
        playerHand[i]=dealHand(deck,2)
    ## Hit Cards
    for i in range(players):
        outcome[i] = hitToConclusion(i)
    dealerOutcome = dealerHitToConclusion()
    ## Evaluate Outcome
    evaluateOutcome(dealerOutcome,outcome)
    
    return outcome
    

def generateDeck():
    values=[str(x) for x in range(1,11)]+['J','Q','K']
    suits=['S','D','H','C']
    deck = []
    for i in values:
        for j in suits:
            deck.append((i,j))
    return deck
    
def dealHand(deck,size):
    hand = deck[:size]
    del deck[:size]
    return hand


def valueHand(hand):
    handValue = 0
    aces = 0
    for i in hand:
        handValue = handValue + values[i[0]]
    pair = False
    if hand[0][0]==hand[1][0]:
        pair = True
    for i in range(len(hand)):
        if hand[i][0]=='1':
            aces = aces+1
    if handValue >21 and aces > 0:
        while aces > 0 and handValue > 21:
            handValue -= 10
            aces -= 1
    return handValue,pair,aces

def hitToConclusion(hand):
    ##Code Up Basic Strategy
def dealerHitToConclusion(hand):
    outcome = 0
    stop = False;
    while stop != True:
        print(hand)
        value, aces = valueHand(hand)[0],valueHand(hand)[2]
        if (value >= 17 and aces==0) or value>17:
            stop = True;
            if value > 21:
                outcome = 0
            else:
                outcome = value
        else:
            hand = hand + dealHand(deck,1)
    return outcome












    
