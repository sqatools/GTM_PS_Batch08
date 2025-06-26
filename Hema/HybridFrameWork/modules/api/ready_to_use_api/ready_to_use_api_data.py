import json
main_api_url = "https://api.restful-api.dev/objects"
users_ids = [4, 7, 9]


create_object_payload = json.dumps({
      "name": "Apple MacBook Pro 200",
      "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "2 TB"
      }
    })

json_headers = {
      'Content-Type': 'application/json'
    }


post_payload1 = json.dumps({
      "name": "Apple MacBook Pro 300",
      "data": {
        "year": 2025,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "3 TB"
      }
    })

put_payload1 = json.dumps({
      "name": "Apple MacBook Pro 500",
      "data": {
        "year": 2030,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "5 TB",
        "RAM": "16 GB"
      }
    })


post_payload2 = json.dumps({
      "name": "Apple iPhone 16",
      "data": {
        "year": 2025,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "3 TB"
      }
    })

patch_payload = json.dumps({
      "name": "Apple iPhone 20",
      "RAM": "12GB",
    })


post_payload3 = json.dumps({
      "name": "Apple iPhone15",
      "data": {
        "year": 2025,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "3 TB"
      }
    })


token_api_url = "https://gorest.co.in/public/v2/users"
access_token = "e8a8639a8982b5c05c84a755a385a72f229072a0da16025f92935606fa41ec86"
auth_headers = {'Authorization': f"Bearer {access_token}"}
