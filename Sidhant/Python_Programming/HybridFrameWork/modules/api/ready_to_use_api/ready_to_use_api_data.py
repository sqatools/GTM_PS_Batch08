import json

main_api_url = "https://api.restful-api.dev/objects"
user_id = [4, 3, 8]

create_object_payload1 = json.dumps({
    "name": "Apple MacBook Pro 160",
    "data": {
        "year": 2019,
        "price": 2849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "2 TB"
    }
})

json_header = {
    'Content-Type': 'application/json'
}

post_payload = json.dumps({
    "name": "Apple MacBook Pro 160",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "2 TB",
        "Ram": "16 GB"
    }
})

put_payload = json.dumps({
    "name": "Apple MacBook Pro 260",
    "data": {
        "year": 2029,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "2 TB"
    }
})

patch_payload = json.dumps({
    "name": "Apple Iphone Pro 160",
})

post_payload1 = json.dumps({
    "name": "Apple MacBook Pro 160",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "2 TB",
        "Ram": "16 GB"
    }
})

token_api_url = "https://gorest.co.in/public/v2/users"
access_token = "a2d5ede9046d79af9f2b53535b33ecb5861b9e1b48c1a53bd035b76b486734f4"
auth_headers = {'Authorization': f"Bearer {access_token}"}
