#1.txt
product 8
order 8
tracking 3
#2.txt
product
order

import re
from collections import Counter, defaultdict

def count_words():
    #Read Content#
    with open("1.txt", "r") as f:
        data = defaultdict(int)
        for line in f:
            key, value = line.strip().split()
            data[key] = int(value)

    with open("2.txt") as f:
    #with open("location_Folder" + file_path, 'r', encoding="utf-8") as f:
        matches = re.findall(r'\b[a-zA-Z]{3,}\b', f.read())
        wordcount = Counter(matches)
        for word, count in wordcount.items():
            data[word] += count                 

    #Write To File
    write_to_file(data)

def write_to_file(data):
    with open("1.txt", "w") as f:
        for word, count in data.items():
            string = word + " " + str(count)
            f.write(string + "\n")
count_words()
