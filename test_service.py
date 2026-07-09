from model import Product
from service import ProductService

product = Product(
    None,
    "Mouse",
    "Electronics",
    "Logitech",
    1200,
    15,
    "XYZ Suppliers",
    "2026-07-08"
)

service = ProductService()

service.add_product(product)

print("Product Added Successfully")