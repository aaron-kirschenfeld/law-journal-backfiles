file_in_name = raw_input("Enter name of file to alter: ") # enter the name of the txt file
file_out_name = raw_input("Enter name of destination file: ") # enter name of new file to write

file_handle = open(file_in_name) # opens the txt file
file_out = open(file_out_name, "w")

for line in file_handle :
    line = line.rstrip()
    if line.endswith(", The") :
        endpt = len(line) - 5
        line = line[:endpt]
        line = "The " + line
    elif line.endswith(", A") :
        endpt = len(line) - 3
        line = line[:endpt]
        line = "A " + line
    elif line.endswith(", An") :
        endpt = len(line) - 4
        line = line[:endpt]
        line = "An " + line
    line = line + "\n"    
    file_out.write(line)
file_out.close()   
