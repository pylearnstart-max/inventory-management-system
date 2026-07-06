from repo import ProductRepo

repo = ProductRepo()

products = repo.get_all_products()

print("========== PRODUCT LIST ==========\n")

for product in products:
    print(product)