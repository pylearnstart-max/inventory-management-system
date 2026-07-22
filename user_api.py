from flask import Blueprint, jsonify, request


from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
    
)

from role_decorator import role_required

from user_model import User
from user_service import UserService
from logger_config import logger


user_api = Blueprint("user_api", __name__)

service = UserService()



# ==========================================
# GET ALL USERS
# ==========================================

@user_api.route("/users", methods=["GET"])
def get_all_users():

    try:

        users = service.get_all_users()

        result = []

        for user in users:

            result.append({

                "user_id": user[0],
                "username": user[1],
                "password": user[2],
                "role": user[3],
                "created_date": str(user[4])

            })


        return jsonify(result),200


    except Exception as e:

        return jsonify({

            "error":str(e)

        }),500




# ==========================================
# GET USER BY ID
# ==========================================

@user_api.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    try:

        user = service.search_user(user_id)


        if user is None:

            return jsonify({

                "message":"User Not Found"

            }),404



        return jsonify({

            "user_id":user[0],
            "username":user[1],
            "password":user[2],
            "role":user[3],
            "created_date":str(user[4])

        }),200



    except Exception as e:

        return jsonify({

            "error":str(e)

        }),500






# ==========================================
# ADD USER
# ==========================================

@user_api.route("/users", methods=["POST"])
def add_user():

    try:

        data = request.get_json()

        # ==========================
        # USERNAME VALIDATION
        # ==========================

        if not data["username"].strip():

            return jsonify({

                "message": "Username is Required"

            }), 400

        # ==========================
        # PASSWORD VALIDATION
        # ==========================

        if not data["password"].strip():

            return jsonify({

                "message": "Password is Required"

            }), 400

        if len(data["password"]) < 6:

            return jsonify({

                "message": "Password must be at least 6 characters"

            }), 400

        # ==========================
        # ROLE VALIDATION
        # ==========================

        if not data["role"].strip():

            return jsonify({

                "message": "Role is Required"

            }), 400

        # ==========================
        # CREATED DATE VALIDATION
        # ==========================

        if not data["created_date"].strip():

            return jsonify({

                "message": "Created Date is Required"

            }), 400

        # ==========================
        # CHECK DUPLICATE USERNAME
        # ==========================

        existing_user = service.search_user_by_username(
            data["username"]
        )

        if existing_user is not None:

            return jsonify({

                "message": "Username Already Exists"

            }), 400

        # ==========================
        # CREATE USER
        # ==========================

        user = User(

            username=data["username"],
            password=data["password"],
            role=data["role"],
            created_date=data["created_date"]

        )

        service.add_user(user)

        return jsonify({

            "message": "User Added Successfully"

        }), 201

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500



# ==========================================
# LOGIN WITH JWT TOKEN
# ==========================================

@user_api.route("/users/login", methods=["POST"])
def login():

    try:

        data = request.get_json()

        # ==========================
        # VALIDATIONS
        # ==========================

        if not data["username"].strip():

            return jsonify({

                "message": "Username is Required"

            }), 400

        if not data["password"].strip():

            return jsonify({

                "message": "Password is Required"

            }), 400

        # ==========================
        # LOGIN
        # ==========================

        user = service.login(

            data["username"],
            data["password"]

        )

        if user is None:

            logger.warning(
                f"Login Failed : {data['username']}"
            )

            return jsonify({

                "message": "Invalid Username or Password"

            }), 401

        # ==========================
        # LOGIN SUCCESS LOG
        # ==========================

        logger.info(
            f"Login Success : {user[1]}"
        )

        token = create_access_token(

            identity=str(user[1]),
            additional_claims={
                "role": user[3]
            }

        )

        return jsonify({

            "message": "Login Successful",

            "token": token

        }), 200

    except Exception as e:

        logger.error(str(e))

        return jsonify({

            "error": str(e)

        }), 500

# ==========================================
# JWT PROFILE
# ==========================================

@user_api.route("/users/profile", methods=["GET"])
@jwt_required()
def profile():

    try:

        current_user = get_jwt_identity()

        return jsonify({

            "message": "Token Valid",
            "user": current_user

        }), 200

    except Exception as e:

        return jsonify({

            "error": str(e)

        }), 500



# ==========================================
# UPDATE USER
# ==========================================

@user_api.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    try:

        data=request.get_json()


        user=User(

            username=data["username"],
            password=data["password"],
            role=data["role"],
            created_date=data["created_date"],
            user_id=user_id

        )


        updated=service.update_user(user)



        if updated:

            return jsonify({

                "message":"User Updated Successfully"

            }),200


        else:

            return jsonify({

                "message":"User Not Found"

            }),404



    except Exception as e:

        return jsonify({

            "error":str(e)

        }),500





# ==========================================
# DELETE USER
# ==========================================

@user_api.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    try:

        deleted=service.delete_user(user_id)


        if deleted:

            return jsonify({

                "message":"User Deleted Successfully"

            }),200


        else:

            return jsonify({

                "message":"User Not Found"

            }),404



    except Exception as e:

        return jsonify({

            "error":str(e)

        }),500
# ==========================================
# MANAGER DASHBOARD
# ==========================================

@user_api.route("/manager/dashboard", methods=["GET"])
@role_required("manager")
def manager_dashboard():
    return jsonify({
        "message": "Welcome Manager"
        }), 200

@user_api.route("/admin/dashboard", methods=["GET"])
@role_required("admin")
def admin_dashboard():

        return jsonify({
          "message": "Welcome Admin"
    }), 200

# ==========================================
# EMPLOYEE DASHBOARD
# ==========================================

@user_api.route("/employee/dashboard", methods=["GET"])
@role_required("employee")
def employee_dashboard():

        return jsonify({
            "message": "Welcome Employee"
        }), 200

    
        