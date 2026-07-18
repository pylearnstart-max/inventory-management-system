ROLE_PERMISSIONS = {


    "admin": [

        "product",
        "supplier",
        "customer",
        "purchase",
        "sales",
        "order",
        "user",
        "dashboard"

    ],



    "manager": [

        "product",
        "supplier",
        "customer",
        "purchase",
        "sales",
        "order",
        "dashboard"

    ],



    "employee": [

        "product_view",
        "customer_view",
        "sales_entry",
        "order_view"

    ]

}



def has_permission(role, module):


    role = role.lower()


    if role in ROLE_PERMISSIONS:


        if module in ROLE_PERMISSIONS[role]:

            return True



    return False