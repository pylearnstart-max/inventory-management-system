from service import ProductService

service = ProductService()

limit = int(input("Enter Low Stock Limit: "))

products = service.get_low_stock_products(limit)

print("\n========== LOW STOCK PRODUCTS ==========\n")

if products:

    for product in products:
        print(product)

else:

    print("No Low Stock Products Found.")