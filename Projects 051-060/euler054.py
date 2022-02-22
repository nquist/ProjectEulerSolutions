# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 21:43:30 2022

@author: nquist
This solves project Euler problem 54. 

Answer: 
Execution Time:  seconds


    IN PROGRESS ----- NOT COMPLETE
"""

import time
start = time.time()

player1_count = 0
player2_count = 0
order = ['2','3','4','5','6','7','8','9','T','J','Q','K', 'A']
order_num = ['02','03','04','05','06','07','08','09','10','11','12','13', '14']
f = open('p054_poker.txt', 'r')

def check_straight(card_nums):
    #vals = [card_nums[x] for x in range(0, len(hand), 3)]
    if 'A' in card_nums:
        for j in order[11:7:-1]:
            if j not in card_nums:
                return 0
    else:
        min_card = min(card_nums)
        idx = order.index(min_card)
        for k in range(idx+1, 4+idx+1):
            if order[k] not in card_nums:
                return 0
    return 1

def check_flush(vals):
    vals_set = set(vals)
    if len(vals_set) == 1:
        return 1
    return 0

def count_multiples(card_nums):
    vals = []
    vals_counter = []
    vals_set = set(card_nums)
    for i in vals_set:
        count = card_nums.count(i)
        vals.append(i)
        vals_counter.append()
    counter = 1*vals_counter
    pair_list = []
    while len(vals_counter) > 0:
        max_val = max(vals_counter)
        
        
    return counter, pair_list
            
def card_hand_sum(hand):
    card_nums = [hand[x] for x in range(0, len(hand), 3)]
    card_suit = [hand[x] for x in range(1, len(hand), 3)]
    bonus_flush = check_flush(card_suit)
    bonus_straight = check_straight(card_nums)
    print(hand, bonus_flush, bonus_straight)
    
    
def count_hand(hand):
    sm = 0
    vals = [hand[x] for x in range(0, len(hand), 3)]
    vals_set = list(set(vals))
    indices = []
    for i in vals_set:
        indices.append(order.index(i))
        val = order_num[order.index(i)]
        sm += int(val)*(vals.count(i)**2)
    return sm*max(indices)
        

for i in range(2):
    line = f.readline()
    hand1 = line[:14]
    hand2 = line[15:-1]
    card_hand_sum(hand1)
    card_hand_sum(hand2)
    #print(hand1, count_hand(hand1))
    #print(hand2, count_hand(hand2))




end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

