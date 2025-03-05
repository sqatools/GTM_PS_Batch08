# Read all email and phone number from given file
def read_email_phone(filepath):
    """
    this function will read file and return all email and phone number from file.

    :param filepath:
    :return:
    """
    email_list = []
    phone_list = []
    # open file
    with open(filepath, "r") as file:
        # read file data
        data = file.read()

        # split file data in word list
        word_list = data.split()
        # apply for loop on word list
        for word in word_list:
            if '@' in word:
                email_list.append(word)
            elif len(word) == 10 and word.isdigit():
                phone_list.append(word)
    return email_list, phone_list


emails, phones = read_email_phone("ReadData.txt")
print("Emails: ", emails)
# Emails:  ['user2@yahoo.com', 'user1@gmail.com', 'user2@facebook.com']
print("Phone Number :", phones)
# Phone Number : ['8845465644', '5445465644', '9954656447']
