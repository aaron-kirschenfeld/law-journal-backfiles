import re

handle = open("fpage_prep.txt")
for line in handle :
    line = line.rstrip()
    stpt = re.findall("\.\s\d+\s\(", line)
    print stpt
    #endpt = line.find("(")
    #line = line[stpt:endpt]
    #print line
