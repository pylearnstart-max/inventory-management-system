from flask import Blueprint, jsonify
import pandas as pd


analytics_api = Blueprint(
    "analytics_api",
    __name__
)



# ==========================================
# LOAD SALES DATA
# ==========================================

def load_data():

    df = pd.read_csv(
        "Sales Analytics Dashboard/sales.csv"
    )

    df["TotalAmount"] = (
        df["Quantity"] *
        df["Price"]
    )

    return df



# ==========================================
# CATEGORY SALES API
# ==========================================

@analytics_api.route(
    "/analytics/category-sales",
    methods=["GET"]
)

def category_sales():

    df = load_data()


    result = (
        df.groupby("Category")
        ["TotalAmount"]
        .sum()
        .reset_index()
        .to_dict(
            orient="records"
        )
    )


    return jsonify({

        "success":True,

        "data":result

    })



# ==========================================
# PRODUCT SALES API
# ==========================================

@analytics_api.route(
    "/analytics/product-sales",
    methods=["GET"]
)

def product_sales():

    df = load_data()


    result = (
        df.groupby("Product")
        ["TotalAmount"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
        .to_dict(
            orient="records"
        )
    )


    return jsonify({

        "success":True,

        "data":result

    })



# ==========================================
# CUSTOMER SALES API
# ==========================================

@analytics_api.route(
    "/analytics/customer-sales",
    methods=["GET"]
)

def customer_sales():

    df = load_data()


    result = (
        df.groupby("Customer")
        ["TotalAmount"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
        .to_dict(
            orient="records"
        )
    )


    return jsonify({

        "success":True,

        "data":result

    })



# ==========================================
# MONTHLY SALES API
# ==========================================

@analytics_api.route(
    "/analytics/monthly-sales",
    methods=["GET"]
)

def monthly_sales():

    df = load_data()


    df["SaleDate"] = pd.to_datetime(
        df["SaleDate"]
    )


    result = (
        df.groupby(
            df["SaleDate"]
            .dt
            .to_period("M")
        )
        ["TotalAmount"]
        .sum()
        .reset_index()
    )


    result["SaleDate"] = (
        result["SaleDate"]
        .astype(str)
    )


    return jsonify({

        "success":True,

        "data":
        result.to_dict(
            orient="records"
        )

    })