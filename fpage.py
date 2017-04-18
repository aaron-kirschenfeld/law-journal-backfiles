handle = open("fpage_prep.txt")
for line in handle :
    line = line.rstrip()
    stpt = line.find("Inst. ") + 6 # this is the line that would benefit from regex most likely  
    endpt = line.find("(")
    line = line[stpt:endpt]
    print line
