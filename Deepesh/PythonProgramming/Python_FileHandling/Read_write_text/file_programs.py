# # Open 1st file in read mode
# f1 = open('append_data.txt', 'r')
# # Open 2nd file in write mode
# f2 = open('writecontent.txt', 'w')
# # Read lines of the file
# lines_list = f1.readlines()
# # Iterate over lines
# for i in range(0, len(lines_list)):
# # Check for odd line
#     if((i+1) % 2!= 0):
#     # Write lines to 2nd file
#         f2.write(lines_list[i])
#     else:
#         pass
# # Close the file
# f1.close()
# f2.close()

# # Open file in read mode with context manager
# with open("long_file.txt", "r") as file:
#     # Read list of lines.
#     FileLines = file.readlines()
#     print(FileLines)
#     # Initial for loop to start picking each line one by one
#     for i in range(len(FileLines)):
#         # Initial for loop to compare all remaining line with previous one.
#         for j in range(i+1, len(FileLines)):
#             # compare each line length, swap small len line with long len line.
#             if len(FileLines[i]) > len(FileLines[j]):
#                 temp = FileLines[i]
#                 FileLines[i] = FileLines[j]
#                 FileLines[j] = temp
#             else:
#                 continue
#
# # re-write all the line one by one to the file
# with open('ReadContent.txt', "w") as file:
#     # Combine all the sequentially arrange lines with join method.
#     all_lines = ''.join(FileLines)
#     # overwrite all the existing lines with new one
#     file.write(all_lines)


def sort_per_line_length(filepath,newfilepath):
    with open(filepath, "r") as file:
        data10 = file.readlines()
        #data10[len(data10)-1]=data10[len(data10)-1]+"\n"
        sortedlinelist =data10.copy()
        for x in range(len(sortedlinelist)):
            for y in range(x+1,len(sortedlinelist)):
                if len(sortedlinelist[y])<len(sortedlinelist[x]):
                    a=sortedlinelist[x]
                    sortedlinelist[x]=sortedlinelist[y]
                    sortedlinelist[y]=a
    with open(newfilepath,"w") as file:
        for i in sortedlinelist:
            file.write(i)
    with open(newfilepath,"r") as file:
        data12=file.read()
        print(data12)
        return data12

sort_per_line_length("long_file.txt","NewSortedContent.txt")
