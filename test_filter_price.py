from service import ProductService

service = ProductService()

min_price = float(input("Enter Minimum Price: "))
max_price = float(input("Enter Maximum Price: "))

products = service.filter_products_by_price(min_price, max_price)

if products:

    print("\n========== Products Found ==========\n")

    for product in products:
        print(product)

else:
    print("No Products Found.")