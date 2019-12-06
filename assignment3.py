import os
import sys
import re
from pprint import pprint
import glob
from importlib import reload
from textblob import TextBlob
import pandas as pd
from collections import Counter

os.chdir('/Users/yamintang/Desktop/FE_595_Financial_Technology/assignment3/download_txt')
# change directory---you can setup your path in ' '

# 1. Merge all of 10 files from people posted on the discussion
# board into a single file with a Python script.

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

reload(sys)
sys.getdefaultencoding()
f = 'female_characters.txt'
f_c = open(f)
female = f_c.read()
blob = TextBlob(female)
np = blob.noun_phrases


# convert list to str

# order the value of polarity


def text(x):
    f_cha = []
    for i in x:
        i = ''.join(i)
        blob = TextBlob(i)
        f_cha.append([blob.sentiment.polarity, i])
    return f_cha


f_char = pd.DataFrame(text(np))
f_char = f_char.sort_values(by=0, ascending=False)


def positive(y):
    key = []
    group_most = []
    __her_data = dict()
    for (i, j) in zip(y[0], y[1]):
        __her_data[j] = i
    for i in __her_data:
            key.append(i)
    for i in range(len(key)):
        if i > 9:
            break
        group_most.append("She's a " + key[i] + ". They fight crime!")
    return group_most

pprint("Best 10 characters:")
pprint(positive(f_char))

# result:
# Best 10 characters:
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


def negative(z):
    key_1 = []
    group_less = []
    __re_data = dict()
    for (i, b) in zip(z[0], z[1]):
        __re_data[b] = i
    for i in __re_data:
        key_1.append(i)
    for i in range(len(key_1)):
        if i > 9:
            break
        group_less.append("She's a " + key_1[len(key_1) - i - 1] + ". They fight crime!")
    return group_less


pprint("Worst 10 characters:")
pprint(negative(f_char))
# Worst 10 characters:
# She's a evil twin sister. They fight crime!
# She's a wrong time. They fight crime!
# She's a wrong places. They fight crime!
# She's a psychotic nymphomaniac vampire. They fight crime!
# She's a wrong side. They fight crime!
# She's a psychotic hypochondriac nun. They fight crime!
# She's a wrong place. They fight crime!
# She's a secret island. They fight crime!
# She's a violent blonde mercenary. They fight crime!
# She's a late maiden aunt. They fight crime!


# group male_characters:
reload(sys)
sys.getdefaultencoding()
m = 'male_characters.txt'
m_c = open(m)
male = m_c.read()
blob = TextBlob(male)
np_m = blob.noun_phrases
# key words


# calculate all noun_phrases polarity
m_char = pd.DataFrame(text(np_m))
m_char = m_char.sort_values(by=0, ascending=False)
# order the value of polarity


def positive_male(y):
    key = []
    group_most = []
    __he_data = dict()
    for (i, j) in zip(y[0], y[1]):
        __he_data[j] = i
    for i in __he_data:
            key.append(i)
    for i in range(len(key)):
        if i > 9:
            break
        group_most.append("he's a " + key[i] + ". They fight crime!")
    return group_most


pprint("Best 10 characters:")
pprint(positive_male(m_char))
# result:
# Best 10 characters:
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


def negative_male(z):
    key_1 = []
    group_less = []
    __re_data = dict()
    for (i, b) in zip(z[0], z[1]):
        __re_data[b] = i
    for i in __re_data:
        key_1.append(i)
    for i in range(len(key_1)):
        if i > 9:
            break
        group_less.append("he's a " + key_1[len(key_1) - i - 1] + ". They fight crime!")
    return group_less


pprint("Worst 10 characters:")
pprint(negative_male(m_char))
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
def common(a):
    __my_data = []
    for i in a[1]:
        __my_data.append(i)
        my_data = Counter(__my_data)
        top_ten = my_data.most_common(10)
    return top_ten


pprint(common(f_char))
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

pprint(common(m_char))
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
