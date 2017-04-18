handle = open("fpage_prep.txt")
for line in handle :
    line = line.rstrip()
    stpt = line.find("Inst. ") + 6
    endpt = line.find("(")
    line = line[stpt:endpt]
    print line
