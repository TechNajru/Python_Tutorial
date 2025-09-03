# python json
# json.dumps() and json.loads()

import json

json_string = '{"name": "Alice", "age": 30}'
data = json.loads(json_string)
print(data["name"])  # ✅ Alice


data = {"name": "Bob", "age": 25}
json_string = json.dumps(data)
print(json_string)


# optional formatting
json_string = json.dumps(data, indent=4, sort_keys=True)
print(json_string)
