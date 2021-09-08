from main.database  import db_connection


class transactionDB:
    def __init__(self):
        pass

    def insert_new_transaction(self, input_dict):

        print("insert_new_transaction method start")
        print("input user dictionary in method insert_new_user ",input_dict)
        tran_date= input_dict["tran_date"]
        withdrawals_ammount = str(input_dict["withdrawals_ammount"])
        deposit_ammount = str(input_dict["deposit_ammount"])
        transfer_fund = str(input_dict["transfer_fund"])
        from_account = str(input_dict["from_account"])
        to_account = str(input_dict["to_account"])
        comment = str(input_dict["comment"])


        # insert_query="insert into user values('"+first_name+"','"+last_name+"',"+dob+",'"+gender+"',"+aadhar+",'"+pan+"',"+None+","+None+","+account_balance+",'"+ifsc_code+"','"+address+"',"+pincode+")"

        db_connect = db_connection.get_mysql_connection()

        cursor = db_connect.cursor()
        cursor.execute("INSERT INTO Transaction(tran_date,withdrawals_ammount,deposit_ammount,transfer_fund,from_account,"
                       "to_account,comment) values (%s,%s,%s,%s,%s,%s,%s)",(tran_date, withdrawals_ammount,
                                                                            deposit_ammount, transfer_fund,
                                                                            from_account, to_account, comment))

        db_connect.commit()
        db_connect.close()
        print("insert_new_user method end")

    def update_user(self, value_dict):
        pass

    def delete_user(self, value_dict):
        pass
