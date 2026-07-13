from stock_model import StockTransaction
from stock_service import StockService


service = StockService()

product_id = int(input("Enter Product ID : "))

transaction_type = input("Enter Type (IN/OUT): ").upper()

quantity = int(input("Enter Quantity : "))

transaction = StockTransaction(
    product_id,
    transaction_type,
    quantity
)

service.add_transaction(transaction)