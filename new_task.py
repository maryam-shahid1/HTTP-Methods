import requests

#GET Method
api_url="https://jsonplaceholder.typicode.com/users/1"
response=requests.get(api_url)
json_response=response.json()
print(json_response)

#POST Method
api_url="https://jsonplaceholder.typicode.com/posts"
new_post = {
    "userId": 10,
    "id": 10,
    "title": "Python practice",
    "body": "Hello, I am Maryam. Nice to meet you!"
  }
json_response=requests.post(api_url,json=new_post)
print(json_response)


