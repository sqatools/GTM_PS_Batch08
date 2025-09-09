import requests
import json


def get_All_objects():
    url = "https://api.restful-api.dev/objects"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())
    print(response.status_code)
    assert len(response.json()) == 13


# get_All_objects()

def get_specific_id_details():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10&id=4"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


get_specific_id_details()


def get_single_id_details(id):
    url = f"https://api.restful-api.dev/objects?id=11/{id}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)


#get_single_id_details("ff8081819782e69e0198abc11eb41fd2")


def create_new_entry_with_post():
    url = "https://api.restful-api.dev/objects"

    payload = json.dumps({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2020,  # This is the request data
            "price": 2849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'  # in header what type of data we are passing is to be mentioned here
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


# create_new_entry_with_post()

def update_data_entry_with_post(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2020,  # This is the request data
            "price": 2849.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "4 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'  # in header what type of data we are passing is to be mentioned here
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)


# update_data_entry_with_post("ff8081819782e69e0198a6229f98120d")

def create_new_entry_with_post_payloaad(request_data):  # Multiple data input through POST method
    url = "https://api.restful-api.dev/objects"

    payload = json.dumps(request_data)
    headers = {
        'Content-Type': 'application/json'  # in header what type of data we are passing is to be mentioned here
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


request_data_list = [
    {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2020,  # This is the request data
            "price": 2849.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "4 TB"
        }
    },
    {
        "name": "Apple MacBook Pro 17",
        "data": {
            "year": 2026,  # This is the request data
            "price": 2849.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "1TB"
        }
    },
    {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2020,  # This is the request data
            "price": 2849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }

]


# for request_body in request_data_list:
# create_new_entry_with_post_payloaad(request_body)


def update_data_entry_with_patch(id):
    url = f"https://api.restful-api.dev/objects/{id}"

    payload = json.dumps({
        "name": "Apple MacBook Advanced Pro",
        "data": {
            "year": 2020,  # This is the request data
            "price": 2849.99,
            "CPU model": "Intel Core i10",
            "Hard disk size": "4 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'  # in header what type of data we are passing is to be mentioned here
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)

    print(response.text)


print("_" * 40)


# update_data_entry_with_patch("ff8081819782e69e0198a6229f98120d")

def delete_data_from_database(id):
    url = f"https://api.restful-api.dev/objects/{id}"
    payload = {}
    headers = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    print(response.text)

# delete_data_from_database("ff8081819782e69e0198a6229f98120d")


def go_test_auth_with_token():
    url = "https://gorest.co.in/public/v2/users"
    access_token = "a2d5ede9046d79af9f2b53535b33ecb5861b9e1b48c1a53bd035b76b486734f4"
    headers = {'Authorization': f"Bearer {access_token}"}
    response = requests.request("GET", url, headers=headers)
    print(response.content)
    print(response.status_code)


go_test_auth_with_token()
