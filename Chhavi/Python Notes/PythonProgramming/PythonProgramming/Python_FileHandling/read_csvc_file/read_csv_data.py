import csv


def read_file(filepath):
    with open(filepath, "r") as file:
        csv_file = csv.reader(file)
        print(csv_file)
        for line in list(csv_file):
            print(line)



read_file("users_data.csv")
"""
['Name', ' Age', ' Email']
['rahul', ' 20', ' rahul@gmail.com']
['rohan', ' 25', ' rohan@yahoo.com']
['rohit', ' 27', ' rohit@hotmail.com']
"""
