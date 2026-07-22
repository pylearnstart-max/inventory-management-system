from flask import Blueprint, jsonify, request


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
    ]

    return jsonify(
        {
            "success": True,
            "report": "Sales By Date Range",
            "total_sales": int(filtered_df["TotalAmount"].sum()),
            "total_orders": len(filtered_df),
            "data": filtered_df.to_dict(orient="records")
        }
    )