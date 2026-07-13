from stock_service import StockService

service = StockService()

transactions = service.get_all_transactions()

print("\n========== STOCK TRANSACTION HISTORY ==========\n")

if transactions:

    for transaction in transactions:
        print(transaction)

else:

    print("No Transactions Found.")