import httpx


from pathlib import Path

from tools.fakers import fake

file_path = Path(__file__).resolve().parent.parent / "testdata" / "files" / "image.png"

files = {"upload_file": open(file_path, "rb")}
body_create = {
    "email": fake.email(),
    "password": "12345",
    "lastName": "Alina_K",
    "firstName": "Testuser",
    "middleName": "Testuser",
}

email = body_create.get("email")

body_login = {"email": email, "password": "12345"}

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

headers = {"Authorization": f"Bearer {login_user_data}"}
create_file = httpx.post(
    "http://localhost:8000/api/v1/files",
    data={"filename": "image.png", "directory": "courses"},
    files={"upload_file": open(file_path, "rb")},
    headers=headers,
)
print(create_file.status_code)
print(create_file.json())
