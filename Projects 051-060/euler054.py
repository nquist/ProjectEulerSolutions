# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 21:43:30 2022

@author: nquist
This solves project Euler problem 54. 

Answer: 376
Execution Time: 0.05199 seconds
"""

import time
start = time.time()

player1_count = 0
player2_count = 0

order_num = ['02','03','04','05','06','07','08','09','10','11','12','13', '14']
dic = {'2':'02','3':'03','4':'04','5':'05','6':'06',
       '7':'07','8':'08','9':'09','T':'10','J':'11',
       'Q':'12','K':'13', 'A':'14'}
f = open('p054_poker.txt', 'r')

def check_straight(card_nums):
    min_card = min(card_nums)
    idx = order_num.index(min_card)
    if idx > 8: return 0
    for k in range(idx+1, 4+idx+1):
        if order_num[k] not in card_nums: return 0
    return 65

def check_flush(vals):
    vals_set = set(vals)
    if len(vals_set) == 1:
        return 75
    return 0

def square_counts(nums):
    vals_counter = []
    vals_set = set(nums)
    sqr_sum = 0
    for i in vals_set:
        count = nums.count(i)
        vals_counter.append(count)
    for j in vals_counter:
        sqr_sum += j**2
    return 10*sqr_sum
            
def calc_prefix(hand):
    nums = [dic[hand[x]] for x in range(0, len(hand), 3)]
    suits = [hand[x] for x in range(1, len(hand), 3)]
    bonus_flush = check_flush(suits)
    bonus_straight = check_straight(nums)
    base = square_counts(nums)
    return base+bonus_flush+bonus_straight


def card_hand_sum(hand):
    nums = [dic[hand[x]] for x in range(0, len(hand), 3)]
    nums_set_list = list(set(nums))
    count_list = []
    num_string = ''
    for i in nums_set_list:
        count = nums.count(i)
        count_list.append([count, i])
    while len(count_list) > 0:
        curr_val = max(count_list)
        idx = count_list.index(curr_val)
        num_string += curr_val[1]*curr_val[0]
        count_list.pop(idx)       
    return num_string
    

for line in f:
    hand1 = line[:14]
    hand2 = line[15:-1]
    hand1_pre = calc_prefix(hand1)
    hand2_pre = calc_prefix(hand2)
    if hand1_pre == hand2_pre:
        hand1_sum = card_hand_sum(hand1)
        hand2_sum = card_hand_sum(hand2)
        if hand1_sum > hand2_sum:
            player1_count += 1
        else:
            player2_count += 1
    elif hand1_pre > hand2_pre:
        player1_count += 1
    else:
        player2_count += 1

print('Player 1 won %i hands and player 2 won %i hands' % (player1_count, player2_count))

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))

