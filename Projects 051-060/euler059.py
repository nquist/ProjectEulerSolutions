# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:45:05 2022

@author: nquist
This solves project Euler problem 59. 

Each character on a computer is assigned a unique code and the preferred standard 
is ASCII (American Standard Code for Information Interchange). For example, 
uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. The advantage 
with the XOR function is that using the same encryption key on the cipher text, 
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. The user would keep the encrypted message 
and the encryption key in different locations, and without both "halves", it is 
impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method 
is to use a password as a key. If the password is shorter than the message, which 
is likely, the key is repeated cyclically throughout the message. The balance for 
this method is using a sufficiently long password key for security, but short 
enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case 
characters. Using p059_cipher.txt, a file containing the encrypted ASCII codes, 
and the knowledge that the plain text must contain common English words, decrypt 
the message and find the sum of the ASCII values in the original text.

Answer: 129448
Execution Time: 0.00500 seconds
"""
import enchant
import time
start = time.time()
en_dict = enchant.Dict("en_US")

f = open('p059_cipher.txt', 'r')
vals = f.readlines()[0].split(',')
available_vals = [i for i in range(65, 90)] + [j for j in range(97, 123)] + [32]
available_vals = set(available_vals)

word_list = []
starting_val = []
for i in range(97, 123):   
    translated = int(vals[0])^i    
    translated2 = int(vals[3])^i
    translated3 = int(vals[6])^i
    translated4 = int(vals[9])^i
    translated5 = int(vals[12])^i
    if (translated in available_vals) and (translated2 in available_vals) and (translated3 in available_vals) and (translated4 in available_vals) and (translated5 in available_vals):
        starting_val.append(i)

middle_val = []
for i in range(97, 123):
    translated = int(vals[1])^i
    translated2 = int(vals[4])^i
    translated3 = int(vals[7])^i
    translated4 = int(vals[10])^i
    if (translated in available_vals) and (translated2 in available_vals) and (translated3 in available_vals) and (translated4 in available_vals):
        middle_val.append(i)

last_val = []
for i in range(97, 123):
    translated = int(vals[2])^i
    translated2 = int(vals[5])^i
    if (translated in available_vals) and (translated2 in available_vals):
        last_val.append(i)

combos = []
for m in starting_val:
    for j in middle_val:
        for k in last_val:
            words = ''
            for l in range(0, 5):
                words += chr(int(vals[3*l])^m)+chr(int(vals[3*l+1])^j)+chr(int(vals[3*l+2])^k)
            first_idx = words.index(' ')
            second_idx = words[first_idx+1:].index(' ') + first_idx
            first_word = words[:first_idx]
            second_word = words[first_idx+1:second_idx+1]
            if en_dict.check(first_word) and en_dict.check(second_word):
                word_list.append(words)
                combos.append([m, j, k])

char_sum = 0
for i in range(0, len(vals), 3):
    char_sum += int(vals[i])^combos[0][0]
    char_sum += int(vals[i+1])^combos[0][1]
    char_sum += int(vals[i+2])^combos[0][2]

print('The sum is %i' % char_sum)

end = time.time()
print("The time of execution of above program is %.05f seconds" % (end-start))