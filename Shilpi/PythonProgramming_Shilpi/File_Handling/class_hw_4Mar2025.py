#Q3 : Read content from file1 and file2 and add content to the file3.

def main():
    text1=fileRead("file1.txt")
    text2=fileRead("file2.txt")
    text3=text1+"\n\n"+text2
    filewrite(text3,"file3.txt")
    textwritten=fileRead("file3.txt")
    print(textwritten)


def fileRead(filepath):
    with open(filepath,"r") as file1:
        textread=file1.read()
        return textread

def filewrite(content1,filepath):
    with open(filepath,"w") as file2:
        textwrite=file2.write(content1)


if __name__=="__main__":
    main()