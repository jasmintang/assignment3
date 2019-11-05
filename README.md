# assignment3

In the previous assignment we scraped data from the “They Fight Crime” joke website. We now have hundreds upon hundreds of
characters. Your task will be several steps:
1. Create a new git project for this assignment.

2. Merge all of the various files from people posted on the discussion board into a single file with a Python script.
Based on the your own files
source_dir = ""#input your file location
os.chdir = ""input your file location
Female_characters_paths = glob.glob(source_dir + "/#your download file name#*.txt")
Male_characters_paths = glob.glob(source_dir + "/your download file name#*.txt")

3.Write a second script that finds the best and worst character of each gender (based on sentiment analysis) and groups 
them together into the original format of the joke. (Reminder: He’s, She’s, They fight crime!)


4.Write a third script that finds the 10 most common descriptions for char- acters.
Finally, write a ReadMe.txt for your project that explains to a user how to use your scripts. Your ReadMe does not need to explain how the scripts work (the scripts should have comments that describe that inline), they need to explain how I can run it on my own set of “They Fight Crime” data.
