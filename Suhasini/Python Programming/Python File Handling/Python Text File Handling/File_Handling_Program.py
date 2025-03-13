# Read all Emails and Phone number from a file
from Anupama.python_practice.homework.dictionary.Py_dictionary import word_list


def read_email_phone(filepath):
    """
    This function will read file and return the list of emails and
    phone numbers.
    :param file_path:
    :return:
    """

    email_list = []
    phone_list = []
    with open (filepath, "r") as file:
        # read file data
        data = file.read()

    # split file data in word list
    word_list = data.split()

    # Apply loop on word list
    for word in word_list:
        if "@" in word:
            email_list.append(word)

        elif len(word) == 10 and word.isdigit():
            phone_list.append(word)

    return email_list, phone_list

# emails, phones = read_email_phone("read_data.txt")
# print("emails :", emails)
# emails : ['user2@yahoo.com', 'user1@gmail.com', 'user2@facebook.com']
# print("phone numbers :", phones)
# phone numbers : ['8845465644', '5445465644', '9954656447']


# Q2 : replace the specific word in file
def replace_word_from_file(filepath, word1, word2):
    with open(filepath, "r") as file:
        file_data = file.read()

    updated_content = file_data.replace(word1, word2)
    with open(filepath, "w") as file:
        file.write(updated_content)

# replace_word_from_file("read_data.txt", "Suhasini", "JAVA")


############### DOUBT
#Q3 : Read content from file1 and file2 and add content to the file3.

def read_file1_and_file2(filepath1, filepath2):
    with open(filepath1, "r") as file1:
        file3 = file1.read()

    with open(filepath2, "r") as file2:
        file22 = file2.read()
        file3 = file3 + file22
        print(file3)

read_file1_and_file2("read_data.txt", "read_data1.txt")

