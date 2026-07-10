from exceptions import ProductValidationError


class ProductValidator:

    @staticmethod
    def validate(product):

        if not product.product_name.strip():
            raise ProductValidationError("Product Name cannot be empty.")

        if not product.category.strip():
            raise ProductValidationError("Category cannot be empty.")

        if not product.brand.strip():
            raise ProductValidationError("Brand cannot be empty.")

        if product.unit_price <= 0:
            raise ProductValidationError("Unit Price must be greater than 0.")

        if product.quantity < 0:
            raise ProductValidationError("Quantity cannot be negative.")

        if not product.supplier_name.strip():
            raise ProductValidationError("Supplier Name cannot be empty.")

        if not product.created_date.strip():
            raise ProductValidationError("Created Date cannot be empty.")