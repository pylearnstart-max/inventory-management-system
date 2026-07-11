from service import ProductService

service = ProductService()

products = service.generate_inventory_report()

print("\n========== INVENTORY REPORT ==========\n")

if products:

    for product in products:
        print(product)

else:
    print("No Products Found.")