from flask import Blueprint, jsonify, request

from customer_model import Customer
from customer_repo import CustomerRepo
from customer_service import CustomerService

customer_api = Blueprint("customer_api", __name__)

repo = CustomerRepo()
service = CustomerService(repo)


# ==========================================
# GET ALL CUSTOMERS
# ==========================================

@customer_api.route("/customers", methods=["GET"])
def get_all_customers():

    try:

        customers = service.get_all_customers()

        result = []

        for customer in customers:

            result.append({

                "customer_id": customer[0],
                "customer_name": customer[1],
                "phone": customer[2],
                "email": customer[3],
                "address": customer[4],
                "created_date": str(customer[5])

            })

        return jsonify(result), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# GET CUSTOMER BY ID
# ==========================================

@customer_api.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):

    try:

        customer = service.get_customer_by_id(customer_id)

        if customer is None:

            return jsonify({
                "message": "Customer Not Found"
            }), 404

        return jsonify({

            "customer_id": customer[0],
            "customer_name": customer[1],
            "phone": customer[2],
            "email": customer[3],
            "address": customer[4],
            "created_date": str(customer[5])

        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# ADD CUSTOMER
# ==========================================

@customer_api.route("/customers", methods=["POST"])
def add_customer():

    try:

        data = request.get_json(silent=True)

        if data is None:

            return jsonify({
                "message": "Invalid JSON Body"
            }), 400

        customer = Customer(

            customer_name=data["customer_name"],
            phone=data["phone"],
            email=data["email"],
            address=data["address"],
            created_date=data["created_date"]

        )

        service.add_customer(customer)

        return jsonify({
            "message": "Customer Added Successfully"
        }), 201

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# UPDATE CUSTOMER
# ==========================================

@customer_api.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):

    try:

        data = request.get_json(silent=True)

        if data is None:

            return jsonify({
                "message": "Invalid JSON Body"
            }), 400

        customer = Customer(

            customer_name=data["customer_name"],
            phone=data["phone"],
            email=data["email"],
            address=data["address"],
            created_date=data["created_date"],
            customer_id=customer_id

        )

        service.update_customer(customer)

        return jsonify({
            "message": "Customer Updated Successfully"
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# DELETE CUSTOMER
# ==========================================

@customer_api.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):

    try:

        service.delete_customer(customer_id)

        return jsonify({
            "message": "Customer Deleted Successfully"
        }), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==========================================
# SEARCH CUSTOMER
# ==========================================

@customer_api.route("/customers/search", methods=["GET"])
def search_customer():

    try:

        keyword = request.args.get("keyword")

        if keyword is None or keyword.strip() == "":

            return jsonify({
                "message": "Keyword is required"
            }), 400

        customers = service.search_customer(keyword)

        result = []

        for customer in customers:

            result.append({

                "customer_id": customer[0],
                "customer_name": customer[1],
                "phone": customer[2],
                "email": customer[3],
                "address": customer[4],
                "created_date": str(customer[5])

            })

        return jsonify(result), 200

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500