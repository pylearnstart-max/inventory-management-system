from supplier_repo import SupplierRepo


class SupplierService:

    def __init__(self):
        self.repo = SupplierRepo()

    def add_supplier(self, supplier):
        self.repo.add_supplier(supplier)

    def get_all_suppliers(self):
        return self.repo.get_all_suppliers()

    def search_supplier(self, supplier_name):

        return self.repo.search_supplier(supplier_name)