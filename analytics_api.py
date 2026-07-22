from flask import Blueprint, jsonify, request, send_file
import pandas as pd
import matplotlib.pyplot as plt
import uuid

analytics_api = Blueprint(
    "analytics_api",
    __name__
)


# ==========================================
# LOAD SALES DATA
# ==========================================

def load_sales_data():

    df = pd.read_csv(
        "Sales Analytics Dashboard/sales.csv"
    )

    df["TotalAmount"] = (
        df["Quantity"] *
        df["Price"]
    )

    return df


# ==========================================
# CATEGORY SALES
# ==========================================

@analytics_api.route(
    "/analytics/category-sales",
    methods=["GET"]
)
def category_sales():

    df = load_sales_data()

    data = (
        df.groupby("Category")["TotalAmount"]
        .sum()
        .reset_index()
        .to_dict(orient="records")
    )

    return jsonify(
        {
            "success": True,
            "report": "Category Wise Sales",
            "data": data
        }
    )


# ==========================================
# PRODUCT SALES
# ==========================================

@analytics_api.route(
    "/analytics/product-sales",
    methods=["GET"]
)
def product_sales():

    df = load_sales_data()

    data = (
        df.groupby("Product")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .to_dict(orient="records")
    )

    return jsonify(
        {
            "success": True,
            "report": "Product Wise Sales",
            "data": data
        }
    )


# ==========================================
# CUSTOMER SALES
# ==========================================

@analytics_api.route(
    "/analytics/customer-sales",
    methods=["GET"]
)
def customer_sales():

    df = load_sales_data()

    data = (
        df.groupby("Customer")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .to_dict(orient="records")
    )

    return jsonify(
        {
            "success": True,
            "report": "Customer Wise Sales",
            "data": data
        }
    )


# ==========================================
# MONTHLY SALES
# ==========================================

@analytics_api.route(
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
            df["SaleDate"].dt.to_period("M")
        )["TotalAmount"]
        .sum()
        .reset_index()
    )

    data["SaleDate"] = (
        data["SaleDate"]
        .astype(str)
    )

    return jsonify(
        {
            "success": True,
            "report": "Monthly Sales Trend",
            "data": data.to_dict(
                orient="records"
            )
        }
    )
# ==========================================
# DASHBOARD SUMMARY API
# ==========================================

@analytics_api.route(
    "/analytics/dashboard-summary",
    methods=["GET"]
)
def dashboard_summary():

    df = load_sales_data()

    total_orders = len(df)

    total_sales = int(
        df["TotalAmount"].sum()
    )

    total_quantity = int(
        df["Quantity"].sum()
    )

    average_sale = round(
        df["TotalAmount"].mean(),
        2
    )

    top_product = (
        df.groupby("Product")
        ["TotalAmount"]
        .sum()
        .idxmax()
    )

    top_customer = (
        df.groupby("Customer")
        ["TotalAmount"]
        .sum()
        .idxmax()
    )

    return jsonify(
        {
            "success": True,
            "dashboard": {

                "total_orders":
                total_orders,

                "total_sales":
                total_sales,

                "total_quantity":
                total_quantity,

                "average_sale":
                average_sale,

                "top_product":
                top_product,

                "top_customer":
                top_customer

            }
        }
    )


# ==========================================
# TOP 5 PRODUCTS API
# ==========================================

@analytics_api.route(
    "/analytics/top-products",
    methods=["GET"]
)
def top_products():

    df = load_sales_data()

    data = (
        df.groupby("Product")
        ["TotalAmount"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(5)
        .reset_index()
        .to_dict(
            orient="records"
        )
    )

    return jsonify(
        {
            "success": True,
            "report": "Top 5 Products",
            "data": data
        }
    )


# ==========================================
# TOP 5 CUSTOMERS API
# ==========================================

@analytics_api.route(
    "/analytics/top-customers",
    methods=["GET"]
)
def top_customers():

    df = load_sales_data()

    data = (
        df.groupby("Customer")
        ["TotalAmount"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(5)
        .reset_index()
        .to_dict(
            orient="records"
        )
    )

    return jsonify(
        {
            "success": True,
            "report": "Top 5 Customers",
            "data": data
        }
    )


# ==========================================
# HIGHEST SALE API
# ==========================================

@analytics_api.route(
    "/analytics/highest-sale",
    methods=["GET"]
)
def highest_sale():

    df = load_sales_data()

    highest = df.loc[
        df["TotalAmount"].idxmax()
    ]

    return jsonify(
        {
            "success": True,
            "report": "Highest Sale",
            "data": highest.to_dict()
        }
    )


# ==========================================
# LOWEST SALE API
# ==========================================

@analytics_api.route(
    "/analytics/lowest-sale",
    methods=["GET"]
)
def lowest_sale():

    df = load_sales_data()

    lowest = df.loc[
        df["TotalAmount"].idxmin()
    ]

    return jsonify(
        {
            "success": True,
            "report": "Lowest Sale",
            "data": lowest.to_dict()
        }
    )


# ==========================================
# SALES SUMMARY API
# ==========================================

@analytics_api.route(
    "/analytics/sales-summary",
    methods=["GET"]
)
def sales_summary():

    df = load_sales_data()

    summary = {

        "total_orders":
        len(df),

        "total_sales":
        int(df["TotalAmount"].sum()),

        "total_quantity":
        int(df["Quantity"].sum()),

        "average_sale":
        round(df["TotalAmount"].mean(), 2)

    }

    return jsonify(
        {
            "success": True,
            "report": "Sales Summary",
            "data": summary
        }
    )
# ==========================================
# COMPLETE DASHBOARD API
# ==========================================

@analytics_api.route(
    "/analytics/dashboard",
    methods=["GET"]
)
def dashboard():

    df = load_sales_data()

    summary = {
        "total_orders": len(df),
        "total_sales": int(df["TotalAmount"].sum()),
        "total_quantity": int(df["Quantity"].sum()),
        "average_sale": round(df["TotalAmount"].mean(), 2),
        "top_product": (
            df.groupby("Product")["TotalAmount"]
            .sum()
            .idxmax()
        ),
        "top_customer": (
            df.groupby("Customer")["TotalAmount"]
            .sum()
            .idxmax()
        )
    }

    category_sales = (
        df.groupby("Category")["TotalAmount"]
        .sum()
        .reset_index()
        .to_dict(orient="records")
    )

    product_sales = (
        df.groupby("Product")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .to_dict(orient="records")
    )

    customer_sales = (
        df.groupby("Customer")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .to_dict(orient="records")
    )

    monthly_sales = (
        df.assign(
            SaleDate=pd.to_datetime(
                df["SaleDate"]
            ).dt.to_period("M").astype(str)
        )
        .groupby("SaleDate")["TotalAmount"]
        .sum()
        .reset_index()
        .to_dict(orient="records")
    )

    top_products = (
        df.groupby("Product")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
        .to_dict(orient="records")
    )

    top_customers = (
        df.groupby("Customer")["TotalAmount"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
        .to_dict(orient="records")
    )

    return jsonify(
        {
            "success": True,
            "summary": summary,
            "category_sales": category_sales,
            "product_sales": product_sales,
            "customer_sales": customer_sales,
            "monthly_sales": monthly_sales,
            "top_products": top_products,
            "top_customers": top_customers
        }
    )


# ==========================================
# SALES BY DATE RANGE API
# ==========================================

@analytics_api.route(
    "/analytics/date-range",
    methods=["GET"]
)
def sales_by_date_range():

    df = load_sales_data()

    start = request.args.get("start")
    end = request.args.get("end")

    if not start or not end:

        return jsonify(
            {
                "success": False,
                "message": "Please provide start and end dates."
            }
        ), 400

    df["SaleDate"] = pd.to_datetime(df["SaleDate"])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    filtered_df = df[
        (df["SaleDate"] >= start) &
        (df["SaleDate"] <= end)
    ].copy()

    filtered_df["SaleDate"] = (
        filtered_df["SaleDate"]
        .dt.strftime("%Y-%m-%d")
    )

    return jsonify(
        {
            "success": True,
            "report": "Sales By Date Range",
            "total_sales": int(
                filtered_df["TotalAmount"].sum()
            ),
            "total_orders": len(filtered_df),
            "data": filtered_df.to_dict(
                orient="records"
            )
        }
    )
# ==========================================
# CATEGORY CHART API
# ==========================================

@analytics_api.route(
    "/analytics/category-chart",
    methods=["GET"]
)
def category_chart():

    df = load_sales_data()

    chart_data = (
        df.groupby("Category")
        ["TotalAmount"]
        .sum()
        .reset_index()
    )

    labels = chart_data["Category"].tolist()

    values = chart_data["TotalAmount"].tolist()


    return jsonify(
        {
            "success": True,
            "chart": "Category Sales Chart",
            "labels": labels,
            "values": values
        }
    )



# ==========================================
# PRODUCT CHART API
# ==========================================

@analytics_api.route(
    "/analytics/product-chart",
    methods=["GET"]
)
def product_chart():

    df = load_sales_data()

    chart_data = (
        df.groupby("Product")
        ["TotalAmount"]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
        .reset_index()
    )


    return jsonify(
        {
            "success": True,
            "chart": "Top Products Chart",
            "labels":
            chart_data["Product"].tolist(),

            "values":
            chart_data["TotalAmount"].tolist()
        }
    )



# ==========================================
# MONTHLY CHART API
# ==========================================

@analytics_api.route(
    "/analytics/monthly-chart",
    methods=["GET"]
)
def monthly_chart():

    df = load_sales_data()


    df["SaleDate"] = pd.to_datetime(
        df["SaleDate"]
    )


    chart_data = (
        df.groupby(
            df["SaleDate"]
            .dt
            .to_period("M")
        )
        ["TotalAmount"]
        .sum()
        .reset_index()
    )


    chart_data["SaleDate"] = (
        chart_data["SaleDate"]
        .astype(str)
    )


    return jsonify(
        {
            "success": True,
            "chart": "Monthly Sales Chart",

            "labels":
            chart_data["SaleDate"].tolist(),

            "values":
            chart_data["TotalAmount"].tolist()
        }
    )

# ==========================================
# EXPORT EXCEL API
# ==========================================

@analytics_api.route(
    "/analytics/export-excel",
    methods=["GET"]
)
def export_excel():

    df = load_sales_data()

    file_name = "sales_report.xlsx"

    df.to_excel(
        file_name,
        index=False
    )

    return send_file(
        file_name,
        as_attachment=True,
        download_name="sales_report.xlsx"
    )
@analytics_api.route(
    "/analytics/category-chart-image",
    methods=["GET"]
)
def category_chart_image():

    df = load_sales_data()

    data = (
        df.groupby("Category")
        ["TotalAmount"]
        .sum()
    )


    plt.figure(figsize=(8,5))

    plt.bar(
        data.index,
        data.values
    )

    plt.title(
        "Category Wise Sales"
    )

    plt.xlabel(
        "Category"
    )

    plt.ylabel(
        "Total Sales"
    )


    file_name = (
        str(uuid.uuid4())
        + ".png"
    )


    plt.savefig(file_name)

    plt.close()


    return send_file(
        file_name,
        mimetype="image/png"
    )