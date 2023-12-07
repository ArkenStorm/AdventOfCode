from collections import Counter
from functools import reduce

inFile = open('../inputs/Day7.txt', 'r')
# inFile = open('2023/inputs/test.txt')
lines = inFile.read().splitlines()

print('Day 7 - Camel Cards')

# Part 1
card_values = { card: i for i, card in enumerate('X23456789TJQKA') }

def get_hand_type(hand: str):
    hand_types = [(1,1,1,1,1), (1,1,1,2), (1,2,2), (1,1,3), (2,3), (1,4), (5,)]
    return hand_types.index(tuple(sorted(Counter(hand).values())))

def hand_strength(hand: str, jokers: bool):
    if jokers:
        hand = hand.replace('J', 'X')
    converted_hand = [card_values[c] for c in hand]  # used for breaking ties
    if 'X' in hand:
        possible_types = [get_hand_type(hand.replace('X', wild)) for wild in '23456789TQKA']
        return (max(possible_types), *converted_hand)
    else:
        return (get_hand_type(hand), *converted_hand)
    
winnings = []
for jokers in [False, True]: 
	pairs = sorted((hand_strength(hand, jokers), int(bid)) for hand, bid in (l.split() for l in lines))
	winnings.append(reduce(lambda acc, i: acc + ((i+1) * pairs[i][1]), range(len(pairs)), 0))

print(f"Part 1: {winnings[0]}")
print(f"Part 2: {winnings[1]}")