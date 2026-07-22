from app import app

client = app.test_client()

response = client.get("/analytics/dashboard")

print(response.status_code)
print(response.json)