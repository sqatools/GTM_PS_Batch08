# Open 1st file in read mode
f1 = open('readcontent.txt', 'r')
# Open 2nd file in write mode
f2 = open('writecontent.txt', 'w')
# Read lines of the file
lines_list = f1.readlines()
# Iterate over lines
for i in range(0, len(lines_list)):
# Check for odd line
    if(i+1) % 2!= 0:
    # Write lines to 2nd file
        f2.write(lines_list[i])
    else:
        pass
# Close the file
f1.close()
f2.close()
