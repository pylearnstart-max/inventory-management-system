from service import ProductService

service = ProductService()

product_id = int(input("Enter Product ID: "))
quantity = int(input("Enter Quantity to Add: "))

service.stock_in(product_id, quantity)