from flask import Flask, jsonify
from flask_jwt_extended import JWTManager

from product_api import product_api
from customer_api import customer_api
from supplier_api import supplier_api
from user_api import user_api
from analytics_api import analytics_api

from flask_swagger_ui import get_swaggerui_blueprint
from flask import render_template



app = Flask(__name__)



# ==========================================
# SWAGGER CONFIGURATION
# ==========================================

SWAGGER_URL = "/swagger"

API_URL = "/static/swagger.json"



swagger_ui_blueprint = get_swaggerui_blueprint(

    SWAGGER_URL,

    API_URL,

    config={

        "app_name":
        "Inventory Management System API"

    }

)



app.register_blueprint(

    swagger_ui_blueprint,

    url_prefix=SWAGGER_URL

)



# ==========================================
# JWT CONFIGURATION
# ==========================================

app.config["JWT_SECRET_KEY"] = (
    "inventory_secret_key"
)



jwt = JWTManager(app)



# ==========================================
# REGISTER BLUEPRINTS
# ==========================================


app.register_blueprint(
    product_api
)


app.register_blueprint(
    customer_api
)


app.register_blueprint(
    supplier_api
)


app.register_blueprint(
    user_api
)


# Sales Analytics APIs

app.register_blueprint(
    analytics_api
)



# ==========================================
# HOME API
# ==========================================


@app.route("/")
def home():

    return jsonify(

        {

            "success": True,

            "message":
            "Inventory Management System API Running"

        }

    )



# ==========================================
# HEALTH CHECK API
# ==========================================


@app.route("/health")
def health():

    return jsonify(

        {

            "status":
            "Application Running"

        }

    )



# ==========================================
# 404 ERROR HANDLER
# ==========================================


@app.errorhandler(404)

def not_found(error):

    return jsonify(

        {

            "success": False,

            "message":
            "API Not Found"

        }

    ),404



# ==========================================
# 500 ERROR HANDLER
# ==========================================


@app.errorhandler(500)

def internal_server_error(error):

    return jsonify(

        {

            "success": False,

            "message":
            "Internal Server Error"

        }

    ),500



# ==========================================
# GLOBAL EXCEPTION HANDLER
# ==========================================


@app.errorhandler(Exception)

def handle_exception(error):

    return jsonify(

        {

            "success": False,

            "message":
            str(error)

        }

    ),500
# ==========================================
# DASHBOARD PAGE
# ==========================================

@app.route("/dashboard")
def dashboard_page():

    return render_template(
        "dashboard.html"
    )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )


