import httpx

from config import settings

body = {"email": "my_usr@example.com", "password": "12345"}
login_user = httpx.post(
    f"{settings.http_client.client_url}/api/v1/authentication/login", json=body
)
login_user_data = login_user.json().get("token").get("accessToken")

headers = {"Authorization": f"Bearer {login_user_data}"}
get_user = httpx.get(
    f"{settings.http_client.client_url}/api/v1/users/me", headers=headers
)

print(get_user.status_code)
print(get_user.json())
