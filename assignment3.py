import os
import re
from textblob import TextBlob

os.getcwd()
#get the current directory
os.chdir('/Users/yamintang/Desktop/FE_595_Financial_Technology/assignment3/download_txt')
# change directory---you can setup your path in ' '

#1. Merge all of 10 files from people posted on the discussion
# board into a single file with a Python script.

import glob
# List inflammation data files from the source directory
source_dir = "/Users/yamintang/Desktop/FE_595_Financial_Technology/assignment3/download_txt"
Female_characters_paths = glob.glob(source_dir + "/Female_Characters*.txt")
Male_characters_paths = glob.glob(source_dir + "/Male_Characters*.txt")

for fp in Female_characters_paths:
    with open('female_characters', 'w') as outfile:
        for name in fp:
            with open(fp) as infile:
                for line in infile:
                    outfile.write(line)
                outfile.write('\n')

for fp in Male_characters_paths:
    with open('male_characters', 'w') as outfile:
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
    i=''.join(i)
    blob = TextBlob(i)
    f_cha.append([blob.sentiment.polarity, i])
print(f_cha)

f_char = pd.DataFrame(f_cha)
f_char = f_char.sort_values(by=0, ascending=False)


top_f_char = f_char.head(10)

__theydata=dict()
for (i, j) in zip(f_char[0],f_char[1]):
    __theydata[j] = i
key=[]
for i in __theydata:
    key.append(i)
print("most:")
groupmost=[]
for i in range(len(key)):
    if i > 9:
        break
    groupmost.append("She's a "+key[i]+ ". They fight crime!")

for i in groupmost:
    print(i)


print("\n\nless:")
for i in range(len(key)):
    if i > 9:
        break
    print(key[len(key)-i-1])


# 3.Write a third script that finds the 10 most common descriptions for characters.



from collections import Counter
__mydata=[]
for i in f_char[1]:
    __mydata.append(i)
mydata=Counter(__mydata)

topten= mydata.most_common(10)
for i in topten:
    print(i)
print(topten)




