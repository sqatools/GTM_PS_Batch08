# read all the email and phone number given file.

def read_email_phone(file_path):
    """
    This function will read file and return the list of emails and
    phone numbers.
    :param file_path:
    :return:
    """
    email_list = []
    phone_list = []
    # open file
    with open(file_path, "r") as file:
        # read file data
        data = file.read()

    # split file data in word list
    word_list = data.split()

    # Apply loop on word list
    for word in word_list:
        # check if word contains @, then consider as email
        if "@" in word:
            # append email to email_list
            email_list.append(word)
        # check if word len is 10, and it contains only digit, then consider as phone number.
        elif len(word) == 10 and word.isdigit():
            # append phone number to phone_list
            phone_list.append(word)

    return email_list, phone_list


# emails, phones = read_email_phone("read_data.txt")
# print("emails :", emails)
# # emails : ['user2@yahoo.com', 'user1@gmail.com', 'user2@facebook.com']
# print("phone numbers :", phones)
# phone numbers : ['8845465644', '5445465644', '9954656447']



# Q2 : replace the specific word in file
def replace_word_from_file(filepath, word1, word2):
    with open(filepath, "r") as file:
        file_data = file.read()

    updated_content = file_data.replace(word1, word2)

    with open(filepath, "w") as file:
        file.write(updated_content)

replace_word_from_file("read_data.txt", "Python", "JAVA")


#Q3 : Read content from file1 and file2 and add content to the file3.
