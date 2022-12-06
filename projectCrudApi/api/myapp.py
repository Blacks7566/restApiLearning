import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

class Myapi:

    def get_data(self):
        print("IF you want to get object by id please enter id or PRESS ENTER ")
        id=input("Enter id : ")
        r = requests.get(url = URL+id)
        response = r.json()
        print(response)

    def create_data(self,data):
        json_data = json.dumps(data)
        r = requests.post(url = URL, data=json_data)
        response = r.json()
        print(response)

    def update_data(self,data):
        json_data = json.dumps(data)
        r = requests.put(url = URL, data=json_data)
        response = r.json()
        print(response)

    def delete_data(self):
        id = input("Enter object id to delete object : ")
        data  = {'id':id} 
        json_data = json.dumps(data)
        r = requests.delete(url = URL, data=json_data)
        response = r.json()
        print(response)

ap = Myapi()  # create Myapi object 

# for create object 

data = {
    'name':'lallu',
    'student_class':'bsc',
    'age':22,
    'roll_no':1004
}

# ap.create_data(data)

# for update data id is must

data = {
    'id':'1',
    'name':'Nitin',
    'student_class':'mca',
    'age':24,
    'roll_no':1001
}

# ap.update_data(data)



ap.delete_data()

ap.get_data()
