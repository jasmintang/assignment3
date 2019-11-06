import os
import re
import sys
from importlib import reload
from textblob import TextBlob
import pandas as pd
from collections import Counter

os.getcwd()
# get the current directory
os.chdir('/Users/yamintang/Desktop/FE_595_Financial_Technology/assignment3/download_txt')
# change directory---you can setup your path in ' '

# 1. Merge all of 10 files from people posted on the discussion
# board into a single file with a Python script.

import glob

# List inflammation data files from the source directory
source_dir = "/Users/yamintang/Desktop/FE_595_Financial_Technology/assignment3/download_txt"
Female_characters_paths = glob.glob(source_dir + "/Female_Characters*.txt")
Male_characters_paths = glob.glob(source_dir + "/Male_Characters*.txt")

for fp in Female_characters_paths:
    with open('female_characters.txt', 'w') as outfile:
        for name in fp:
            with open(fp) as infile:
                for line in infile:
                    outfile.write(line)
                outfile.write('\n')

for fp in Male_characters_paths:
    with open('male_characters.txt', 'w') as outfile:
        for name in fp:
            with open(fp) as infile:
                for line in infile:
                    outfile.write(line)
                outfile.write('\n')


# 2.Write a second script that finds the best and worst character of each gender (based on sentiment analysis)
# and groups them together into the original format of the joke. (Reminder: He’s, She’s, They fight crime!)

os.chdir('/Users/yamintang/Desktop/FE_595_Financial_Technology/assignment3/download_txt')
reload(sys)
sys.getdefaultencoding()
f = 'female_characters.txt'
f_c = open(f)
female = f_c.read()
blob = TextBlob(female)
np = blob.noun_phrases
Str_np = ' '.join([str(elem) for elem in np])
# convert list to str

f_cha = []
for i in np:
    i = ''.join(i)
    blob = TextBlob(i)
    f_cha.append([blob.sentiment.polarity, i])
print(f_cha)
# calculate all noun_phrases polarity
f_char = pd.DataFrame(f_cha)
f_char = f_char.sort_values(by=0, ascending=False)
# order the value of polarity

__her_data = dict()
for (i, j) in zip(f_char[0], f_char[1]):
    __her_data[j] = i
key = []
for i in __her_data:
    key.append(i)

print("Best 10 characters:")
group_most = []
for i in range(len(key)):
    if i > 9:
        break
    group_most.append("She's a " + key[i] + ". They fight crime!")

for i in group_most:
    print(i)
# result:
# She's a incredible destiny. They fight crime!
# She's a brilliant psychic archaeologist. They fight crime!
# She's a beautiful gypsy fairy princess. They fight crime!
# She's a pregnant mutant soap star. They fight crime!
# She's a powerful witches. They fight crime!
# She's a wealthy blonde magician 's assistant. They fight crime!
# She's a elegant blonde traffic cop. They fight crime!
# She's a supernatural junkie journalist. They fight crime!
# She's a supernatural mutant nun. They fight crime!
# She's a sarcastic renegade bodyguard. They fight crime!

print("\n\nWorst 10 characters:")
group_less = []
for i in range(len(key)):
    if i > 9:
        break
    group_less.append("She's a " + key[len(key)-i-1] + ". They fight crime!")

for i in group_less:
    print(i)
#Worst 10 characters:
#She's a evil twin sister. They fight crime!
#She's a wrong time. They fight crime!
#She's a wrong places. They fight crime!
#She's a psychotic nymphomaniac vampire. They fight crime!
#She's a wrong side. They fight crime!
#She's a psychotic hypochondriac nun. They fight crime!
#She's a wrong place. They fight crime!
#She's a secret island. They fight crime!
#She's a violent blonde mercenary. They fight crime!
#She's a late maiden aunt. They fight crime!

# group male_characters:
os.chdir('/Users/yamintang/Desktop/FE_595_Financial_Technology/assignment3/download_txt')
reload(sys)
sys.getdefaultencoding()
m = 'male_characters.txt'
m_c = open(m)
male = m_c.read()
blob = TextBlob(male)
np_m = blob.noun_phrases
# key words

m_cha = []
for i in np_m:
    i = ''.join(i)
    blob = TextBlob(i)
    m_cha.append([blob.sentiment.polarity, i])
print(m_cha)
# calculate all noun_phrases polarity
m_char = pd.DataFrame(m_cha)
m_char = m_char.sort_values(by=0, ascending=False)
# order the value of polarity

__him_data = dict()
for (i, j) in zip(m_char[0], m_char[1]):
    __him_data[j] = i
key = []
for i in __him_data:
    key.append(i)

print("Best 10 characters:")
group_most = []
for i in range(len(key)):
    if i > 9:
        break
    group_most.append("He's a " + key[i] + ". They fight crime!")

for i in group_most:
    print(i)
# result:
# He's a true killer. They fight crime!
# He's a fast cars. They fight crime!
# He's a ringling bros. They fight crime!
# He's a voodoo card. They fight crime!
# He's a circus. They fight crime!
# He's a vegetarian shaman. They fight crime!
# He's a cat burglar. They fight crime!
# He's a mysterious suitcase. They fight crime!
# He's a immortal pirate shaman. They fight crime!
# He's a one.\'. They fight crime!


print("\n\nWorst 10 characters:")
group_less = []
for i in range(len(key)):
    if i > 9:
        break
    group_less.append("He's a " + key[len(key)-i-1] + ". They fight crime!")

for i in group_less:
    print(i)
# Worst 10 characters:
# He's a fiendish moralistic cat burglar. They fight crime!
# He's a fiendish albino cowboy. They fight crime!
# He's a shy neurotic cowboy. They fight crime!
# He's a wrong crowd. They fight crime!
# He's a secret government programme. They fight crime!
# He's a notorious alcoholic paramedic. They fight crime!
# He's a alcoholic cowboy. They fight crime!
# He's a alien invasion. They fight crime!
# He's a dead american confidante. They fight crime!
# He's a suave zombie vagrant. They fight crime!





# 3.Write a third script that finds the 10 most common descriptions for characters.

__she_data = []
for i in f_char[1]:
    __she_data.append(i)
she_data = Counter(__she_data)

top_ten = she_data.most_common(10)
for i in top_ten:
    print(i)
print(top_ten)

# female result:
# ('incredible destiny', 303)
# ('satanic', 303)
# ('different time', 303)
# ('mob', 202)
# ('fairy princess', 202)
# ("'s torch", 202)
# ('femme fatale', 202)
# ('liberty', 202)
# ('opera singer', 202)
# ('elvis', 202)

__he_data = []
for i in m_char[1]:
    __he_data.append(i)
he_data = Counter(__he_data)

top_ten = he_data.most_common(10)
for i in top_ten:
    print(i)
print(top_ten)

# male result:
# ('secret government programme', 495)
# ('nobel', 396)
# ('fast cars', 297)
# ('mysterious suitcase', 297)
# ('true killer', 198)
# ('uncanny powers', 198)
# ("wife\\ 's", 198)
# ('alien invasion', 198)
# ('ringling bros', 99)
# ('voodoo card', 99)
