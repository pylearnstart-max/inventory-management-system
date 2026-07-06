from repo import ProductRepo

repo = ProductRepo()

product = repo.get_product_by_id(2)

print(product)