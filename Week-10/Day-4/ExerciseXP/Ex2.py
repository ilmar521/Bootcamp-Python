import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_sampleJson = json.loads(sampleJson)
print(json_sampleJson['company']['employee']['payable']['salary'])
json_sampleJson['company']['employee']['birth_date'] = '1990-05-16'
with open('json_file.json', 'w') as f:
    json.dump(json_sampleJson, f)

