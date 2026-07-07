from model import Product
from repo import ProductRepo

product = Product(
    2,
    "Laptop",
    "Electronics",
    "Dell",
    85000,
    25,
    "ABC Suppliers",
    "2026-07-03"
)

repo = ProductRepo()

repo.update_product(product)