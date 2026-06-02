import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())

data = {"title": "New task", "completed": False, "userId": 1}
response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.json())

data1 = {"username": "test", "password": "12345"}
response = httpx.post("https://httpbin.org/post", data=data1)
print(response.status_code)
print(response.json())
print(response.headers)

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.request.headers)
print(response.json())

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.status_code)
print(response.json())

files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=files)
print(response.json())

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
print(response1.json())
print(response2.json())

client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://httpbin.org/get")
print(response.json())
print(response.status_code)
try:
    response = httpx.get("https://jsonplaceholder.typicode.com/todos/url-un")
    print(response.raise_for_status())
except httpx.HTTPStatusError as e:
    print(f"Error response:{e}")

try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=1)
except httpx.ReadTimeout:
    print("Request limit")
