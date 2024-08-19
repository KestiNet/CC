import json
import os

file_path = 'Z:/devs/CC/ccParser/tests/step2/invalid.json'
#rfile = open(file_path,'r')

with open(file_path, 'r') as file:
    content = file.read()
 
#all_data = json.load(rfile)

is_valid_json = False

try:
   valid = json.loads(content)
   is_valid_json = True
   print("0")
except json.JSONDecodeError:
    is_valid_json = False
    print("1")