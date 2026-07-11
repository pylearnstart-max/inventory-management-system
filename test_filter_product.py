from service import ProductService

service = ProductService()

category = input("Enter Category: ")

products = service.filter_products_by_category(category)

if products:

    print("\n========== Products Found ==========\n")

    for product in products:
        print(product)

else:
    print("\nNo Products Found.")