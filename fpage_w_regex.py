#! python3
# fpage_w_regex.py - Locates the first page of a law journal article from its Bluebook citation


import re

first_page = re.compile(r'\.\s\d+') # to search for one or more digits following a period 
first_page_list = []

# TODO: create and define function here 
# outputs value of the first page as a string to a list 

handle = open("fpage_prep.txt")
for line in handle :
    line = line.rstrip()
    first_page_mo = first_page.search(line)
    if first_page_mo == None:
        continue
    else:
        first_page_string = str(first_page_mo.group())
        first_page_string = first_page_string[2:]
        first_page_list.append(first_page_string)

print(first_page_list)

