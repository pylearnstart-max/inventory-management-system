from model import Product
from repo import ProductRepo

product = Product(
    "Laptop",
    "Electronics",
    "Dell",
    55000,
    10,
    "ABC Suppliers",
    "2026-07-04"
)

repo = ProductRepo()

repo.add_product(product)