from repo import ProductRepo


repo = ProductRepo()

products = repo.get_all_products()

for product in products:
    print(product)