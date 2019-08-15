import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#generating all cards
values=np.array(["7","8","J","Q","K","A","T","9"])
colors=np.array(["c","s","h","d"])
all_cards=np.full((4,8),"empty")
for v in range(8):
    for c in range(4):
        all_cards[c][v]=values[v]+colors[c]
linearized_deck=all_cards.reshape(1,4*8)[0]


def ShuffleAndGiveCards(given_deck):
    #shuffling deck
    np.random.shuffle(given_deck)
    
    
    #dealing cards
    hands_list=[[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
    for p in range(4):
        #turn 1
        hands_list[p][0]=given_deck[3*p:3*p+3]
        #turn 2 
        hands_list[p][1]=given_deck[3*p+12:3*p+3+12]
        #turn 3
        hands_list[p][2]=given_deck[24+p*2:24+p*2+2]
    
    return hands_list

def getValueCard(card):
    if card[0]=='J' or card[0]=='Q' or card[0]=='K':
        return 10
    elif card[0]=='7':
        return 7
    elif card[0]=='8':
        return 8
    elif card[0]=='T':
        return 12
    elif card[0]=='A':
        return 11
    else:
        return 13
    

def getHandValue(hand):
    hand_value=getValueCard(hand[0])
    number_of_cards=len(hand)
    if hand[0][1]==hand[1][1]:
        hand_value+=getValueCard(hand[1])
    elif number_of_cards>2:
        if hand[0][1]==hand[2][1]:
            hand_value+=getValueCard(hand[2])
        elif hand[1][1]==hand[2][1]:
            hand_value=getValueCard(hand[1])+getValueCard(hand[2])
    return hand_value


def getHandsValues(hands_list):
    hands_value=np.empty((4,3))
    for i in range(4):
        for j in range(3):
            hands_value[i][j]=getHandValue(hands_list[i][j])
    return hands_value




games_point_distrib=[]
for i in range(10000):
    hands_list=ShuffleAndGiveCards(linearized_deck)
    games_point_distrib.append(getHandsValues(hands_list))

max_point_each_game_3_cards=[]
for i in range(len(games_point_distrib)):
    for j in range(2):
        max_point_each_game_3_cards.append(max([games_point_distrib[i][0][j],
                                                games_point_distrib[i][1][j],
                                                games_point_distrib[i][2][j],
                                                games_point_distrib[i][3][j]]))

num_bins = 80
n, bins, patches = plt.hist(max_point_each_game_3_cards,num_bins)
plt.show()
