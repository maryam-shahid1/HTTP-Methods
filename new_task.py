import requests

# GET Method
api_url = 'https://jsonplaceholder.typicode.com/users/1'
response = requests.get(api_url)
json_response = response.json()
print(json_response)

# POST Method
api_url = 'https://jsonplaceholder.typicode.com/posts'
new_post = {
    "userId": 10,
    "id": 10,
    "title": "Python practice",
    "body": "Hello, I am Maryam. Nice to meet you!"
}
json_response = requests.post(api_url, json=new_post)
print(json_response)

# PUT Method
api_url = 'https://jsonplaceholder.typicode.com/posts/1'
update_post = {
    "userId": 1,
    "id": 1,
    "title": "The Art of War",
    "body": "An ancient Chinese military "
            "text written by Sun Tzu."
}
response = requests.put(api_url, json=update_post)
json_response = response.json()
print(json_response)

# PATCH Method
patch_post = {"title": "The Odyssey"}
response = requests.patch(api_url, json=patch_post)
json_response = response.json()
print(json_response)

# DELETE Method
response = requests.delete(api_url)
json_response = response.json()
print(json_response)
