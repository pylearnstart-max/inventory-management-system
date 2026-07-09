from service import ProductService

service = ProductService()

products = service.get_all_products()

for product in products:
    print(product)