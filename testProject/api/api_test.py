import requests
import json



# URL = "http://127.0.0.1:8000/stuApi/"
URL = "http://127.0.0.1:8000/stucreate/"


class EmployeeApi:

    def get(self):
        print("If you want to data by id enter id or press Enter and continue...")
        print()
        self.id = input("Enter id : ")
        r = requests.get(url=URL+self.id)
        data = r.json()
        print(data)
    
    def post(self,data):
        json_data = json.dumps(data)
        r = requests.post(url=URL,data = json_data)
        response = r.json()
        print(response)


e1 = EmployeeApi()

# e1.get()

data = {
    'employee_name':'soniji',
    'employee_roll':'driver',
    'employee_age':24,
    'employee_salary':10000
}

e1.post(data)
