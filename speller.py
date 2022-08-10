"""
Problem is spell check

Implement a spell-checker

argv[0] is speller.py

"""
from sys import argv
import re, time
import sys

from dictionary import check,load,size,unload

LENGTH = 45

# python has no constant explicity but other has generally
# Captalize will tells others to get it as Constant
# path of dictionaries txt files 

DICTIONARY = "dictionaries/large"

if len(argv) != 2 and len(agrv) != 3:
    print("Usage : speller [dictionary] text")
    sys.exit(1)

time_check,time_load,time_size,time_unload = 0.0,0.0,0.0,0.0

dictionary = arv[1] if len(argv) == 3 else DICTIONARY

before = time.process_time()
loaded = load(dictionary)
after = time.process_time()

if not loaded:
    exit(f"Could not load {dictionary}.")

time_load = after - before

text = argv[2] if len(argv) == 3 else argv[1]
file = open(text,"r",enconding="latin_1")
if not file:
    print(f"Could not open {text}.")
    unload()
    sys.exit(1)

print("\nMISSPELLED WORDS\n")

index,misspellings,words = 0,0,0

word = ""

while True:
    c = file.read(1)
    if not c:
        break
    if re.match(r"[A-Za-Z]") or (c == "'" and index > 0):
        word +=c
        index +=1
    if index > LENGTH:
        while True:
            c = file.read(1)
            if not c or not re.match(r"[A-Za-z]",c):
                break;
        
        index , word = 0 , ""

    elif c.isdigit():

        while True:

            c = file.read(1)
            if not c or (not c.isalpha() and not c.isdigit()):
                break

            index , word =0, ""

        elif index > 0:

            words += 1
            before = time.process_time()
            misspelled = check(word)
            after = time.process_time()

            time_check += after - before

            if misspelled:
                print(word)
                misspelling += 1

            index , word = 0, ""

file.close()

before = time.process_time()
n = size()
after = time.process_time()

time_size = after - before

before = time.process_time()
unloaded = unload()
after = time.process_time()

if not 

























