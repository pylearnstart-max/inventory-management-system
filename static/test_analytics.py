from app import app

client = app.test_client()

apis = [
    "/analytics/category-sales",
    "/analytics/product-sales",
    "/analytics/customer-sales",
    "/analytics/monthly-sales",
    "/analytics/dashboard-summary",
    "/analytics/top-products",
    "/analytics/top-customers",
    "/analytics/highest-sale",
    "/analytics/lowest-sale",
    "/analytics/sales-summary",
    "/analytics/dashboard",
    "/analytics/date-range?start=2026-07-01&end=2026-07-05"
]

for api in apis:
    print("=" * 60)
    print("API :", api)
    print("=" * 60)

    response = client.get(api)

    print("Status Code :", response.status_code)
    print(response.json)
    print()