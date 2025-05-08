import requests
# pip install requests.

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

def get_single_id_details():
    url = "https://api.restful-api.dev/objects/12"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

get_single_id_details()
