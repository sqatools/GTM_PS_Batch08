def single_dict(d , key_1='',sep='.'):
     sing_dict={}
     for key,value in d.items():
       new_key=(f"{key_1}{sep}{key}" if key_1 else key)
       if isinstance(value,dict):
        sing_dict.update(single_dict(value,new_key,sep))
       else:
        sing_dict[new_key] = value
     return sing_dict
abc =single_dict(nested_dict)
print(abc)

nested_dict = {
    "id": 1,
    "user": {
        "name": "Alice",
        "city": "New York"
    },
    "account": {
        "type": "premium",
        "active": True
    }
}

# Expected Output:
# {
#     'id': 1,
#     'user-name': 'Alice',
#     'user-city': 'New York',
#     'account-type': 'premium',
#     'account-active': True
# }
