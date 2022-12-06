import requests
import json



URL = "http://127.0.0.1:8000/stuCreate/"

data = {
    'name':'nikki',
    'stu_class':'10th',
    'age':14,
    'roll_no':1001
}


json_data = json.dumps(data)


r = requests.post(url=URL,data=json_data)

res = r.json()

print(res)