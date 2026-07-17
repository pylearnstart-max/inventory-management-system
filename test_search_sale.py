from sales_service import SalesService

service = SalesService()

sale_id = int(input("Enter Sale ID: "))

sale = service.search_sale(sale_id)

print("\n========== SEARCH SALE ==========\n")

if sale:
    print(sale)
else:
    print("Sale Not Found")