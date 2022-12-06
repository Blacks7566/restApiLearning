import requests
import json


data = {
    'name':'gpi',
    'student_class':'12th',
    'age':24,
    'roll_no':1002,
}

URL = "http://127.0.0.1:8000/stuApi/"

class Myapi:

    def get_data(self):
        print("If you want to see data by id enter id or PRESS ENTER.....")
        print()
        id = input("Enter id : ")
        r = requests.get(url = URL+id)
        response = r.json()
        print(response)

    def create_data(self,data):

        json_data = json.dumps(data)
        r = requests.post(url=URL,data = json_data)
        response = r.json()
        print(response)

    def update_data(self,data):


        json_data = json.dumps(data)
        r = requests.put(url = URL,data = json_data)
        response = r.json()
        print(response)

    def delete_data(self):

        id = input("Enter object id for delete data...")
        data = {'id':id}
        json_data = json.dumps(data)
        r = requests.delete(url = URL,data = json_data)
        response = r.json()
        print(response)

api = Myapi()

# api.create_data(data)

# data for update
# data = {'id':3,
#         'name':'golu',
#         'student_class':'10th',
#         'age':16}

# api.update_data(data)


api.delete_data()
api.get_data()