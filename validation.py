class ProductValidator:

    @staticmethod
    def validate(product):

        if not product.product_name.strip():
            raise ValueError("Product Name cannot be empty.")

        if not product.category.strip():
            raise ValueError("Category cannot be empty.")

        if not product.brand.strip():
            raise ValueError("Brand cannot be empty.")

        if product.unit_price <= 0:
            raise ValueError("Unit Price must be greater than 0.")

        if product.quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        if not product.supplier_name.strip():
            raise ValueError("Supplier Name cannot be empty.")

        if not product.created_date.strip():
            raise ValueError("Created Date cannot be empty.")