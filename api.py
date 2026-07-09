from flask import Flask, request
from model import Product
from service import ProductService

app = Flask(__name__)

service = ProductService()


@app.route("/", methods=["GET"])
def home():

    return {
        "message": "Inventory Management API is Running",
        "status": "Success"
    }


@app.route("/products", methods=["POST"])
def add_product():

    data = request.get_json()

    product = Product(
        None,
        data["product_name"],
        data["category"],
        data["brand"],
        data["unit_price"],
        data["quantity"],
        data["supplier_name"],
        data["created_date"]
    )

    service.add_product(product)

    return {
        "message": "Product Added Successfully"
    }, 201
@app.route("/products", methods=["GET"])
def get_all_products():

    products = service.get_all_products()

    result = []

    for product in products:

        result.append({
            "product_id": product.product_id,
            "product_name": product.product_name,
            "category": product.category,
            "brand": product.brand,
            "unit_price": float(product.unit_price),
            "quantity": product.quantity,
            "supplier_name": product.supplier_name,
            "created_date": str(product.created_date)
        })

    return result
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):

    product = service.get_product_by_id(product_id)

    if product is None:
        return {
            "message": "Product Not Found"
        }, 404

    return {
        "product_id": product.product_id,
        "product_name": product.product_name,
        "category": product.category,
        "brand": product.brand,
        "unit_price": float(product.unit_price),
        "quantity": product.quantity,
        "supplier_name": product.supplier_name,
        "created_date": str(product.created_date)
    }
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):

    data = request.get_json()

    product = Product(
        product_id,
        data["product_name"],
        data["category"],
        data["brand"],
        data["unit_price"],
        data["quantity"],
        data["supplier_name"],
        data["created_date"]
    )

    service.update_product(product)

    return {
        "message": "Product Updated Successfully"
    }
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    service.delete_product(product_id)

    return {
        "message": "Product Deleted Successfully"
    }

if __name__ == "__main__":
    app.run(debug=True)