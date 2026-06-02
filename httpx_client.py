import httpx

body_login = {"email": "my_usr1@example.com", "password": "12345"}

login_user_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=body_login
)
access_token = login_user_response.json().get("token").get("accessToken")
print(access_token)

client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {access_token}"},
)

response = client.get("/api/v1/users/me")
print(response.text)
