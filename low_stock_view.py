from product_service import ProductService



def show_low_stock_alert():


    service = ProductService()


    limit = 5


    products = service.get_low_stock_products(limit)



    print("\n====================================")
    print("          LOW STOCK ALERT")
    print("====================================")


    if products:


        print(
            "Product ID | Product Name | Category | Quantity"
        )

        print("------------------------------------")


        for product in products:


            print(
                product[0],
                "|",
                product[1],
                "|",
                product[2],
                "|",
                product[3]
            )


    else:


        print("No Low Stock Products Found.")


    print("====================================")