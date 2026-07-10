from model import Product
from service import ProductService

service = ProductService()

product = Product(
    None,
    "   Laptop   ",
    "   Electronics   ",
    "   Dell   ",
    55000,
    10,
    "   ABC Suppliers   ",
    "   2026-07-10   "
)

try:
    service.add_product(product)

    print("Product Added Successfully")
    print("Product Name :", product.product_name)
    print("Category :", product.category)
    print("Brand :", product.brand)
    print("Supplier :", product.supplier_name)
    print("Created Date :", product.created_date)

except Exception as e:
    print(e)