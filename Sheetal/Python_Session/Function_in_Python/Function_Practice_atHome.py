def add_word(w1, w2) -> str:
    return ((w1) + (w2)), ((w2) * (w1)), ((w2) // (w1)), ((w2) - (w1))


r1, r2, r3, r4 = add_word(20, 30)

print("Result", r1)
print("Result", r2)
print("Result", r3)
print("Result", r4)


# Q2 : replace the specific word in file
def replace_word_from_file(filepath, word1, word2):
    # with open(filepath, "r") as file:
    #     file_data = file.read()
    #     # content = file.read()
    #     print(file_data)
    try:
        with open(filepath, "r") as file:
            file_data = file.read()
            print(file_data)
    except FileNotFoundError:
        print("The file was not found.")

    updated_content = file_data.replace(word1, word2)

    with open(filepath, "w") as file:
        file1 = file.write(updated_content)

        return file1
    print(file1)


replace_word_from_file("D:/PythonAutomation/GTM_PS_Batch08/Sheetal/Python_Session/File_Handling/read_data.txt", "Python", "JAVA")
