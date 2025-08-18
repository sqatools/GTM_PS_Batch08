import json

main_api_url = "https://api.restful-api.dev/objects"
user_id = [4,3,8]

create_object_payload = json.dumps({
      "name": "Apple MacBook Pro 160",
      "data": {
        "year": 2019,
        "price": 1849.99,
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
