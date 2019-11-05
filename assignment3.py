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






