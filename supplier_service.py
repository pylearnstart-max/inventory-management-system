from supplier_repo import SupplierRepo


class SupplierService:

    def __init__(self):
        self.repo = SupplierRepo()

    def add_supplier(self, supplier):
        self.repo.add_supplier(supplier)