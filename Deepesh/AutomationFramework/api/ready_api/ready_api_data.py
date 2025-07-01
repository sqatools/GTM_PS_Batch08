import json

ready_api_url = "https://api.restful-api.dev/objects"
ids_list = [5, 7, 9]
object_details = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}
object_json_payload = json.dumps(object_details)
headers = {
           'Content-Type': 'application/json'
       }


put_object_details = {
   "name": "Apple MacBook Pro 20",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "2 TB",
      "color": "silver"
   }
}

put_object_details_json = json.dumps(put_object_details)

patch_object_details = { "name": "Apple MacBook Pro 25 (Updated Name)" }
patch_object_details_json = json.dumps(patch_object_details)

#############################################
users_details_url = "https://gorest.co.in/public/v2/users"
access_token = "2fcabc17443f5e15070811c38f35b257838683a00fa76ef22471ebd4001ab7b5"
auth_headers = {'Authorization' : f"{access_token}"}
