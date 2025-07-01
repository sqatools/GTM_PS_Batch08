import json

class UtilTools:

    def read_json_content(self, file_path):
        with open(file_path, "r") as f1:
            data = f1.read()
            json_data = json.loads(data)
            return json_data


if __name__ == '__main__':
    obj = UtilTools()
    data = obj.read_json_content("data_file.json")
    print(data)
    print(data['email']) # john@gmail.com
