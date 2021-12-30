import json

import requests

url = 'http://localhost:9000/student'
header = {'Content-type': 'application/json'}
id = '/88'


class Test_Api_Req:

    def test_names_students(self):
        response = requests.get(url + '/list')
        response_json = response.json()
        print(json.dumps(response_json, indent=4))

    def test_post(self):
        payload = {"firstName": "dolev", "lastName": "sigron", "email": "dolevdo189466@gmail.com",
                   "programme": "Financial Analysis"}
        response = requests.post(url, json=payload, headers=header)
        response_json = response.json()
        print(response_json)
        print(response.status_code)
        assert response.status_code == 201

    def test_add_student_courses(self):
        courses = ["Python course", "Csharp course", "Java course"]
        payload = {"firstName": "sali", "lastName": "sigron", "email": "sole678do1894@gmail.com", "programme": "bla bla",
                   "courses": courses}
        response = requests.post(url, json=payload, headers=header)
        response_json = response.json()
        print(response_json)
        print(response.status_code)
        assert response.status_code == 201

    def test_put_student(self):
        payload = {"firstName": "maor", "lastName": "sigron", "email": "555678do1894@gmail.com", "programme": "bla bla"}
        response = requests.put(url+id, json=payload,headers=header)
        response_json = response.json()
        print(response_json)
        print(response.status_code)
        assert response.status_code == 200


    def test_delete_students(self):
        id = '/106'
        response = requests.delete(url + id)
        print(response.status_code)
        assert response.status_code == 204