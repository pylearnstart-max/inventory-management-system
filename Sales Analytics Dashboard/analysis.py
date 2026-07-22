from flask import Blueprint, jsonify
import pandas as pd


analytics_bp = Blueprint(
    "analytics",
    __name__
)


# ==========================================
# LOAD SALES DATA
# ==========================================

def load_sales_data():

    df = pd.read_csv("sales.csv")

    df["TotalAmount"] = (
        df["Quantity"] *
        df["Price"]
    )

    return df



# ==========================================
# CATEGORY WISE SALES API
# ==========================================

@analytics_bp.route(
    "/analytics/category-sales",
    methods=["GET"]
)

def category_sales():

    df = load_sales_data()


    data = (
        df.groupby("Category")
        ["TotalAmount"]
        .sum()
        .reset_index()
    )


    result = data.to_dict(
        orient="records"
    )


    return jsonify(
        {
            "success":True,
            "report":"Category Wise Sales",
            "data":result
        }
    )



# ==========================================
# PRODUCT WISE SALES API
# ==========================================

@analytics_bp.route(
    "/analytics/product-sales",
    methods=["GET"]
)

def product_sales():

    df = load_sales_data()


    data = (
        df.groupby("Product")
        ["TotalAmount"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )


    result = data.to_dict(
        orient="records"
    )


    return jsonify(
        {
            "success":True,
            "report":"Product Wise Sales",
            "data":result
        }
    )



# ==========================================
# CUSTOMER WISE SALES API
# ==========================================

@analytics_bp.route(
    "/analytics/customer-sales",
    methods=["GET"]
)

def customer_sales():

    df = load_sales_data()


    data = (
        df.groupby("Customer")
        ["TotalAmount"]
        .sum()
        .sort_values(
            ascending=False
        )
        .reset_index()
    )


    result = data.to_dict(
        orient="records"
    )


    return jsonify(
        {
            "success":True,
            "report":"Customer Wise Sales",
            "data":result
        }
    )



# ==========================================
# MONTHLY SALES TREND API
# ==========================================

@analytics_bp.route(
    "/analytics/monthly-sales",
    methods=["GET"]
)

def monthly_sales():

    df = load_sales_data()


    df["SaleDate"] = pd.to_datetime(
        df["SaleDate"]
    )


    data = (
        df.groupby(
            df["SaleDate"]
            .dt
            .to_period("M")
        )
        ["TotalAmount"]
        .sum()
        .reset_index()
    )


    data["SaleDate"] = (
        data["SaleDate"]
        .astype(str)
    )


    result = data.to_dict(
        orient="records"
    )


    return jsonify(
        {
            "success":True,
            "report":"Monthly Sales Trend",
            "data":result
        }
    )