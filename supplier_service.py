class SupplierService:

    def __init__(self, repo):

        self.repo = repo

    # ==========================================
    # ADD SUPPLIER
    # ==========================================

    def add_supplier(self, supplier):

        self.repo.add_supplier(supplier)

    # ==========================================
    # GET ALL SUPPLIERS
    # ==========================================

    def get_all_suppliers(self):

        return self.repo.get_all_suppliers()

    # ==========================================
    # GET SUPPLIER BY ID
    # ==========================================

    def search_supplier(self, supplier_id):

        return self.repo.search_supplier(supplier_id)

    # ==========================================
    # SEARCH SUPPLIER BY NAME
    # ==========================================

    def search_supplier_by_name(self, supplier_name):

        return self.repo.search_supplier_by_name(supplier_name)

    # ==========================================
    # UPDATE SUPPLIER
    # ==========================================

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

    # ==========================================
    # DELETE SUPPLIER
    # ==========================================

    def delete_supplier(self, supplier_id):

        return self.repo.delete_supplier(supplier_id)

    # ==========================================
    # SUPPLIER REPORT
    # ==========================================

    def supplier_report(self):

        return self.repo.supplier_report()