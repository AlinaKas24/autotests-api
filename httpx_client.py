import httpx

from config import settings

body_login = {"email": "my_usr1@example.com", "password": "12345"}

login_user_response = httpx.post(
    f"{settings.http_client.client_url}/api/v1/authentication/login", json=body_login
)
access_token = login_user_response.json().get("token").get("accessToken")
print(access_token)

client = httpx.Client(
    base_url=f"{settings.http_client.client_url}",
    timeout=settings.http_client.timeout,
    headers={"Authorization": f"Bearer {access_token}"},
)

response = client.get("/api/v1/users/me")
print(response.text)
