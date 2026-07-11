from service import ProductService

service = ProductService()

brand = input("Enter Brand: ")

products = service.filter_products_by_brand(brand)

if products:

    print("\n========== Products Found ==========\n")

    for product in products:
        print(product)

else:
    print("No Products Found.")