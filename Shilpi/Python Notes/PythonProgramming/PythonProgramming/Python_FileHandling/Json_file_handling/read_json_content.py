import json



def read_json_data(filepath):
    with open(filepath, "r") as file:
        data = file.read()
        print(type(data))
        json_data = json.loads(data)
        print(type(json_data))
        return json_data


data = read_json_data("users_data.json")
print(data)
print("first name :", data['firstname'])
print("last name :", data['lastname'])
print("email :", data['email'])
print("social link :", data['social_link'])
print("hobbies details :", data['hobbies'])
print("hobbies details :", data['hobbies'][3]["age"])
data["city"] = "Mumbai"


def write_json_data(filepath, new_content):
    with open(filepath, "w") as file:
        print(new_content)
        json_dump = json.dumps(new_content)
        print(json_dump)
        file.write(json_dump)

write_json_data("users_data3.json", data)


# json.loads() method :  when we read json content from json file and wants to convert in normal dictionary
#                        then we have to use json.loads() method.

# json.dumps() method :  when we want to convert a normal dictionary to json content then we have
#                         to use json.dumps() method.
