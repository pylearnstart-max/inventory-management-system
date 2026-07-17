from sales_service import SalesService

service = SalesService()

sales = service.get_all_sales()

print("=" * 40)
print("        ALL SALES")
print("=" * 40)

if sales:

    for sale in sales:
        print(sale)

else:
    print("No Sales Found")