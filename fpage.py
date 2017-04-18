handle = open("fpage_prep.txt")
for line in handle :
    line = line.rstrip()
    stpt = line.find("Inst. ") + 6 # this is the line that would benefit from regex most likely; here, it's set to find from the text "Inst.", which was the first journal I used this on.  
    endpt = line.find("(")
    line = line[stpt:endpt]
    print line
