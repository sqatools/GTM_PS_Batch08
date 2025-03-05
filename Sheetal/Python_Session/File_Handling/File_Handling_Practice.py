# Q2 : replace the specific word in file
def replace_word_from_file(filepath, word1, word2):
    with open(filepath, "r") as file:
        file_data = file.read()
        print(file_data)

    updated_content = file_data.replace(word1, word2)

    with open(filepath, "w") as file:
        file.write(updated_content)

    with open(filepath, "r") as file:
        file1 = file.read()
        print("\nUpdated file content:\n", file1)

replace_word_from_file("read_data.txt", "Java", "Python")
