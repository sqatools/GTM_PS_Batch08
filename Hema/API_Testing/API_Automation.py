import requests
# pip install requests.
import json

def get_All_objects():

    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.status_code)
    print(response.json())
    assert len(response.json()) == 13

#get_All_objects()


def get_specific_ids_details():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


#get_specific_ids_details()

def get_single_id_details(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

#get_single_id_details(12)

def create_new_entry_with_post():

    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
      "name": "Apple MacBook Pro 160",
      "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "2 TB"
      }
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    # {"id":"ff808181932badb60196876cbb431a03","name":"Apple MacBook Pro 160","createdAt":"2025-04-30T15:59:32.163+00:00","data":{"year":2019,"price":1849.99,"CPU model":"Intel Core i9","Hard disk size":"2 TB"}}


#create_new_entry_with_post()
#get_single_id_details("ff808181932badb60196876cbb431a03")



def update_data_entry_with_post(id):

    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
      "name": "Apple MacBook Pro 200",
      "data": {
        "year": 2025,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "3 TB"
      }
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload)
    print(response.text)

update_data_entry_with_post("ff808181932badb60196876cbb431a03")


def create_new_entry_with_post_payload(request_data):

    url = "https://api.restful-api.dev/objects"

    payload = json.dumps(request_data)
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

request_data_list = [
                {
      "name": "Apple MacBook Pro 200",
      "data": {
        "year": 2025,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "3 TB"
      }
    },

    {
      "name": "Apple MacBook Pro 201",
      "data": {
        "year": 2026,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "4 TB"
      }
    },

    {
      "name": "Apple MacBook Pro 202",
      "data": {
        "year": 2027,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "5 TB"
      }
    },
]
print("_"*50)
for request_body in request_data_list:
    create_new_entry_with_post_payload(request_body)



def update_data_entry_with_patch(id):

    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
      "name": "Apple MacBook Ad Pro",
    })
    headers = {
      'Content-Type': 'application/json'
    }
    response = requests.request("PATCH", url, headers=headers, data=payload)
    print(response.text)

print("_"*50)
#update_data_entry_with_patch("ff808181932badb60196876cbb431a03")

def delete_data_from_database(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = {}
    headers = {
    }
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)
    

delete_data_from_database("ff808181932badb60196876cbb431a03")
get_single_id_details("ff808181932badb60196876cbb431a03")
