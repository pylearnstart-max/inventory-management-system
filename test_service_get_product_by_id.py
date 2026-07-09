from service import ProductService

service = ProductService()

product = service.get_product_by_id(4)

print(product)