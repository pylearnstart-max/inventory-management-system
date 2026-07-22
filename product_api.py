from flask import Blueprint, jsonify, request

from model import Product
from product_repo import ProductRepo
from product_service import ProductService

product_api = Blueprint("product_api", __name__)

repo = ProductRepo()
service = ProductService(repo)


# ==========================================
# GET ALL PRODUCTS
# ==========================================

@product_api.route("/products", methods=["GET"])
def get_all_products():

    try:

        products = service.get_all_products()

        result = []

        for product in products:

            result.append({
                "product_id": product[0],
                "product_name": product[1],
                "category": product[2],
                "brand": product[3],
                "unit_price": float(product[4]),
                "quantity": product[5],
                "supplier_name": product[6],
                "created_date": str(product[7])
            })

        return jsonify(result), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# GET PRODUCT BY ID
# ==========================================

@product_api.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):

    try:

        product = service.search_product(product_id)

        if product is None:

            return jsonify({
                "message": "Product Not Found"
            }), 404

        result = {
            "product_id": product[0],
            "product_name": product[1],
            "category": product[2],
            "brand": product[3],
            "unit_price": float(product[4]),
            "quantity": product[5],
            "supplier_name": product[6],
            "created_date": str(product[7])
        }

        return jsonify(result), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# ADD PRODUCT
# ==========================================

@product_api.route("/products", methods=["POST"])
def add_product():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "message": "Request body is required"
            }), 400

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

        return jsonify({
            "message": "Product Added Successfully"
        }), 201

    except KeyError as e:

        return jsonify({
            "error": f"Missing field: {e}"
        }), 400

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# UPDATE PRODUCT
# ==========================================

@product_api.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "message": "Request body is required"
            }), 400

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

        return jsonify({
            "message": "Product Updated Successfully"
        }), 200

    except KeyError as e:

        return jsonify({
            "error": f"Missing field: {e}"
        }), 400

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# DELETE PRODUCT
# ==========================================

@product_api.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    try:

        service.delete_product(product_id)

        return jsonify({
            "message": "Product Deleted Successfully"
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500