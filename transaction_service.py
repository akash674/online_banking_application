from main.database.transactions_sql import transactionDB
class TransactionService:
    def __init__(self):
        self.transactiondb=transactionDB()


    def create_transaction_id(self):
        print("welcome to transaction_id create page")
        print()
        tran_date=input("please enter date: ")
        withdrawals_ammount= float(input("please enter withdrawals_ammount:"))
        deposit_ammount=float(input("please enter deposit_ammount:"))
        transfer_fund=float(input("please enter transfer_fund:"))
        from_account=int(int(input("please enter from_account:")))
        to_account=int(input("please enter to_account:"))
        comment=input("please enter comment:")


        input_dict={}
        input_dict["tran_date"]=tran_date
        input_dict["withdrawals_ammount"] = withdrawals_ammount
        input_dict["deposit_ammount"] = deposit_ammount
        input_dict["transfer_fund"] = transfer_fund
        input_dict["from_account"] = from_account
        input_dict["to_account"] = to_account
        input_dict["comment"] = comment


        print("input from transaction in dictionary:")
        print(input_dict)

        self.transactiondb.insert_new_transaction(input_dict)


