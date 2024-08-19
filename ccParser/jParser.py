import json
import os

file_paths = ['tests/step1/invalid.json', 'tests/step1/valid.json']

all_data = []

for file_path in file_paths:
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            all_data.append(data)
    else:
        print(f"File not found: {file_path}")

for idx, data in enumerate(all_data):
    if  json.loads(all_data):
        print(f"true")
    else:
        print(f"False")
    
    
    
    #print(f"Data from file {file_paths[idx]}: {data}")