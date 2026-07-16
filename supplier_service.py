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
    def update_supplier(self, supplier):

        self.repo.update_supplier(supplier)
    def delete_supplier(self, supplier_id):

        self.repo.delete_supplier(supplier_id)
    def get_supplier_report(self):

        self.repo.get_supplier_report()