import json

def read_json_data(filepath):
    with open(filepath) as file:
        data= file.read()
        json_data = json.loads(data)
        return json_data

data=read_json_data("test.json")
print(data)
print("first name",data['Name'])
print("last name",data['lastname'])
print("email",data['email'])
print("hobbies",data['hobbies'])
print("social",data['social'])
print("hobbies",data['hobbies'],[3],["age"])
