from flask import Blueprint, jsonify, request

from supplier_model import Supplier
from supplier_repo import SupplierRepo
from supplier_service import SupplierService

supplier_api = Blueprint("supplier_api", __name__)

repo = SupplierRepo()
service = SupplierService(repo)


# ==========================================
# GET ALL SUPPLIERS
# ==========================================

@supplier_api.route("/suppliers", methods=["GET"])
def get_all_suppliers():

    try:

        suppliers = service.get_all_suppliers()

        result = []

        for supplier in suppliers:

            result.append({

                "supplier_id": supplier[0],
                "supplier_name": supplier[1],
                "phone": supplier[2],
                "email": supplier[3],
                "address": supplier[4],
                "created_date": str(supplier[5])

            })

        return jsonify(result), 200

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# ==========================================
# GET SUPPLIER BY ID
# ==========================================

@supplier_api.route("/suppliers/<int:supplier_id>", methods=["GET"])
def get_supplier(supplier_id):

    try:

        supplier = service.search_supplier(supplier_id)

        if supplier is None:

            return jsonify({

                "message": "Supplier Not Found"

            }), 404

        return jsonify({

            "supplier_id": supplier[0],
            "supplier_name": supplier[1],
            "phone": supplier[2],
            "email": supplier[3],
            "address": supplier[4],
            "created_date": str(supplier[5])

        }), 200

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# ==========================================
# ADD SUPPLIER
# ==========================================

@supplier_api.route("/suppliers", methods=["POST"])
def add_supplier():

    try:

        data = request.get_json(silent=True)

        if data is None:

            return jsonify({

                "message": "Invalid JSON Body"

            }), 400

        supplier = Supplier(

            supplier_name=data["supplier_name"],
            phone=data["phone"],
            email=data["email"],
            address=data["address"],
            created_date=data["created_date"]

        )

        service.add_supplier(supplier)

        return jsonify({

            "message": "Supplier Added Successfully"

        }), 201

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# ==========================================
# UPDATE SUPPLIER
# ==========================================

@supplier_api.route("/suppliers/<int:supplier_id>", methods=["PUT"])
def update_supplier(supplier_id):

    try:

        data = request.get_json(silent=True)

        if data is None:

            return jsonify({

                "message": "Invalid JSON Body"

            }), 400

        updated = service.update_supplier(

            supplier_id,
            data["phone"],
            data["email"],
            data["address"]

        )

        if updated:

            return jsonify({

                "message": "Supplier Updated Successfully"

            }), 200

        else:

            return jsonify({

                "message": "Supplier Not Found"

            }), 404

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# ==========================================
# DELETE SUPPLIER
# ==========================================

@supplier_api.route("/suppliers/<int:supplier_id>", methods=["DELETE"])
def delete_supplier(supplier_id):

    try:

        deleted = service.delete_supplier(supplier_id)

        if deleted:

            return jsonify({

                "message": "Supplier Deleted Successfully"

            }), 200

        else:

            return jsonify({

                "message": "Supplier Not Found"

            }), 404

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# ==========================================
# SEARCH SUPPLIER BY NAME
# ==========================================

@supplier_api.route("/suppliers/search/<string:supplier_name>", methods=["GET"])
def search_supplier_by_name(supplier_name):

    try:

        suppliers = service.search_supplier_by_name(supplier_name)

        result = []

        for supplier in suppliers:

            result.append({

                "supplier_id": supplier[0],
                "supplier_name": supplier[1],
                "phone": supplier[2],
                "email": supplier[3],
                "address": supplier[4],
                "created_date": str(supplier[5])

            })

        return jsonify(result), 200

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500


# ==========================================
# SUPPLIER REPORT
# ==========================================

@supplier_api.route("/suppliers/report", methods=["GET"])
def supplier_report():

    try:

        report = service.supplier_report()

        return jsonify({

            "total_suppliers": report[0]

        }), 200

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500