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
    value_card1=getValueCard(hand[0])
    value_card2=getValueCard(hand[1])
    hand_value=max(value_card1,value_card2)
    number_of_cards=len(hand)
    if hand[0][1]==hand[1][1]:
        hand_value=value_card1+value_card2
    if number_of_cards>2:
        value_card3=getValueCard(hand[2])
        hand_value=max(hand_value,value_card3)
        if hand[0][1]==hand[2][1]:
            hand_value=value_card1+value_card3
        if hand[0][1]==hand[1][1]:
            hand_value=value_card1+value_card2
        if hand[1][1]==hand[2][1]:
            hand_value=value_card2+value_card3
        if (hand[0][1]==hand[2][1]) and (hand[0][1]==hand[1][1]):
            hand_value=value_card1+value_card2+value_card3
    return hand_value


def getHandsValues(hands_list):
    hands_value=np.empty((4,3))
    for i in range(4):
        for j in range(3):
            hands_value[i][j]=getHandValue(hands_list[i][j])
    return hands_value




games_point_distrib=[]
for i in range(100000):
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

max_point_each_game_2_cards=[]
for i in range(len(games_point_distrib)):
    max_point_each_game_2_cards.append(max([games_point_distrib[i][0][2],
                                                games_point_distrib[i][1][2],
                                                games_point_distrib[i][2][2],
                                                games_point_distrib[i][3][2]]))

num_bins = 80
n, bins, patches = plt.hist(max_point_each_game_2_cards,num_bins)
plt.show()

possible_values=[7,8,10,11,12,13,15,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

total_size=len(max_point_each_game_3_cards)
count_each_values=np.zeros((1,len(possible_values)))
for j in range(len(possible_values)):
    count_each_values[0][j]=max_point_each_game_3_cards.count(possible_values[j])


prop_of_hands_beaten=np.empty((1,len(possible_values)))
for k in range(len(possible_values)):
    partial_sum=0
    for j in range(k):
        partial_sum+=count_each_values[0][j+1]
    prop_of_hands_beaten[0][k]=partial_sum/total_size

plt.bar(possible_values, prop_of_hands_beaten[0], width=0.8,align='center', data=None)
plt.show()

possible_values2=[7,8,10,11,12,13,15,17,18,19,20,21,22,23,24,25]

total_size2=len(max_point_each_game_2_cards)
count_each_values2=np.zeros((1,len(possible_values2)))
for j in range(len(possible_values2)):
    count_each_values2[0][j]=max_point_each_game_2_cards.count(possible_values2[j])


prop_of_hands_beaten2=np.empty((1,len(possible_values2)))
for k in range(len(possible_values2)):
    partial_sum2=0
    for j in range(k):
        partial_sum2+=count_each_values2[0][j+1]
    prop_of_hands_beaten2[0][k]=partial_sum2/total_size2

plt.bar(possible_values2, prop_of_hands_beaten2[0], width=0.8,align='center', data=None)
plt.show()
    

