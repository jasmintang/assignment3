import os
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

# Iterate over the files

for fp in os.listdir(Female_characters_paths):
    file_female = fp)
    print(file_female)
# Open the source file in read mode
    with open(fp, 'r') as f:
#Parse the output file name, combine the result_dir folder-path and the filename of the input file
    output_fp = os.path.join(result_dir, file_female)


