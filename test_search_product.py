from service import ProductService

service = ProductService()

product_name = input("Enter Product Name to Search: ")

products = service.search_product_by_name(product_name)

if products:
    print("\nProducts Found:\n")

    for product in products:
        print(product)

else:
    print("No Product Found.")