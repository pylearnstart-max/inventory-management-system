from supplier_repo import SupplierRepo


class SupplierService:


    def __init__(self, repo=None):

        if repo is None:
            repo = SupplierRepo()

        self.repo = repo


    def add_supplier(self, supplier):

        return self.repo.add_supplier(
            supplier
        )


    def get_all_suppliers(self):

        return self.repo.get_all_suppliers()


    def search_supplier(self, supplier_id):

        return self.repo.search_supplier(
            supplier_id
        )


    def search_supplier_by_name(self, supplier_name):

        return self.repo.search_supplier_by_name(
            supplier_name
        )


    def update_supplier(
            self,
            supplier_id,
            phone,
            email,
            address
    ):

        return self.repo.update_supplier(
            supplier_id,
            phone,
            email,
            address
        )


    def delete_supplier(self, supplier_id):

        return self.repo.delete_supplier(
            supplier_id
        )