from service import ProductService

service = ProductService()

product_id = int(input("Enter Product ID: "))
quantity = int(input("Enter Quantity to Remove: "))

service.stock_out(product_id, quantity)