from model import Product
from service import ProductService

product = Product(
    1,
    "Gaming Laptop",
    "Electronics",
    "Dell",
    75000,
    30,
    "ABC Suppliers",
    "2026-07-08"
)

service = ProductService()

service.update_product(product)