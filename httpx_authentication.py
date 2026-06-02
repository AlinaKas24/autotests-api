import httpx

body = {"email": "my_usr@example.com", "password": "12345"}
login_user = httpx.post("http://localhost:8000/api/v1/authentication/login", json=body)
login_user_data = login_user.json().get("token").get("refreshToken")
print(login_user.status_code)
print(login_user.json())
print(login_user_data)

body_refresh = {"refreshToken": login_user_data}
refresh = httpx.post(
    "http://localhost:8000/api/v1/authentication/refresh", json=body_refresh
)
print(refresh.status_code)
print(refresh.json())
