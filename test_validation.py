from model import Product
from service import ProductService
from exceptions import ProductValidationError

service = ProductService()


def test_product(product):

    try:
        service.add_product(product)
        print("Validation Passed")

    except ProductValidationError as e:
        print(e)


print("========== Test Case 1 : Empty Product Name ==========")

product = Product(
    None,
    "",
    "Electronics",
    "Dell",
    55000,
    10,
    "ABC Suppliers",
    "2026-07-10"
)

test_product(product)


print("\n========== Test Case 2 : Empty Category ==========")

product = Product(
    None,
    "Laptop",
    "",
    "Dell",
    55000,
    10,
    "ABC Suppliers",
    "2026-07-10"
)

test_product(product)


print("\n========== Test Case 3 : Empty Brand ==========")

product = Product(
    None,
    "Laptop",
    "Electronics",
    "",
    55000,
    10,
    "ABC Suppliers",
    "2026-07-10"
)

test_product(product)


print("\n========== Test Case 4 : Invalid Unit Price ==========")

product = Product(
    None,
    "Laptop",
    "Electronics",
    "Dell",
    -100,
    10,
    "ABC Suppliers",
    "2026-07-10"
)

test_product(product)


print("\n========== Test Case 5 : Invalid Quantity ==========")

product = Product(
    None,
    "Laptop",
    "Electronics",
    "Dell",
    55000,
    -5,
    "ABC Suppliers",
    "2026-07-10"
)

test_product(product)


print("\n========== Test Case 6 : Empty Supplier Name ==========")

product = Product(
    None,
    "Laptop",
    "Electronics",
    "Dell",
    55000,
    10,
    "",
    "2026-07-10"
)

test_product(product)


print("\n========== Test Case 7 : Empty Created Date ==========")

product = Product(
    None,
    "Laptop",
    "Electronics",
    "Dell",
    55000,
    10,
    "ABC Suppliers",
    ""
)

test_product(product)


print("\n========== Test Case 8 : Valid Product ==========")

product = Product(
    None,
    "Laptop",
    "Electronics",
    "Dell",
    55000,
    10,
    "ABC Suppliers",
    "2026-07-10"
)

test_product(product)