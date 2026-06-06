import httpx

from tools.fakers import fake

body_create = {
    "email": fake.email(),
    "password": "12345",
    "lastName": "Alina_K",
    "firstName": "Testuser",
    "middleName": "Testuser",
}

email = body_create.get("email")

body_login = {"email": email, "password": "12345"}
body_update = {
    "email": fake.email(),
    "lastName": "Alina_Kas",
    "firstName": "Testuser",
    "middleName": "Testuser",
}

print("Create user")
create_user = httpx.post("http://localhost:8000/api/v1/users", json=body_create)
user_id = create_user.json().get("user").get("id")
print(create_user.status_code)
print(create_user.json())
print(user_id)

print("Login user")
login_user = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=body_login
)
login_user_data = login_user.json().get("token").get("accessToken")
print(login_user_data)

client = httpx.Client(headers={"Authorization": f"Bearer {login_user_data}"})

print("Get user me")
get_user = client.get("http://localhost:8000/api/v1/users/me")
print(get_user.status_code)
print(get_user.json())
print(get_user.request.headers)

print("Get user by id")
params = {"userId": user_id}
get_user_by_id = client.get(f"http://localhost:8000/api/v1/users/{user_id}")
print(get_user_by_id.status_code)
print(get_user_by_id.json())

print("Update user")
update_user = client.patch(
    f"http://localhost:8000/api/v1/users/{user_id}", json=body_update
)
print(update_user.status_code)
print(update_user.json())

print("Get user by id")
get_user_by_id = client.get(f"http://localhost:8000/api/v1/users/{user_id}")
print(get_user_by_id.status_code)
print(get_user_by_id.json())

print("Delete user by id")
delete_user = client.delete(f"http://localhost:8000/api/v1/users/{user_id}")
print(delete_user.status_code)
