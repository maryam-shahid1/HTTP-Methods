import requests

#GET method
api_url="https://jsonplaceholder.typicode.com/todos"
response=requests.get(api_url)
todo_list=response.json()
incomplete=[]

for todo in todo_list:
    if todo['completed'] == False:
        incomplete.append(todo)

print(incomplete)

#POST method
new_todo={"userId":10, "id":2, "title":"things to do", "completed":False}
response=requests.post(api_url,json=new_todo)
post_response=response.json()
print(post_response)

#PUT method
api_url="https://jsonplaceholder.typicode.com/todos/4"
response=requests.get(api_url)
response.json()

updated_todo={"userId": 1, "id":4,"title": "Pay Bills", "completed": False}
response=requests.put(api_url, json=updated_todo)
put_response=response.json()
print(put_response)

# PATCH method
todo={"completed":True}
response=requests.patch(api_url,json=todo)
patch_response=response.json()
print(patch_response)

 #DELETE method
response=requests.delete(api_url)
response.json()
print(response.status_code)