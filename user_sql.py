from main.database import db_connection


class UserDB:
    def __init__(self):
        pass

    def insert_new_user(self, input_dict):

        print("insert_new_user method start")
        print("input user dictionary in method insert_new_user ",input_dict)
        first_name = input_dict["first_name"]
        last_name = input_dict["last_name"]
        dob = input_dict["dob"]
        gender = input_dict["gender"]
        aadhar = str(input_dict["aadhar"])
        pan = input_dict["pan"]
        account_balance = str(input_dict["account_balance"])
        ifsc_code = input_dict["ifsc_code"]
        address = input_dict["address"]
        pincode = str(input_dict["pincode"])

        # insert_query="insert into user values('"+first_name+"','"+last_name+"',"+dob+",'"+gender+"',"+aadhar+",'"+pan+"',"+None+","+None+","+account_balance+",'"+ifsc_code+"','"+address+"',"+pincode+")"

        db_connect = db_connection.get_mysql_connection()

        cursor = db_connect.cursor()
        cursor.execute("INSERT INTO user(first_name,last_name,dob,gender,aadhar,pan,net_banking_id,"
                       "net_banking_password,account_balance,ifsc_code,address,pincode) VALUES (%s,%s,%s,%s,%s,%s,%s,"
                       "%s,%s,%s,%s,%s)", (
            first_name, last_name, dob, gender, aadhar, pan, None, None, account_balance, ifsc_code, address, pincode))

        db_connect.commit()
        db_connect.close()
        print("insert_new_user method end")

    def update_user(self, value_dict):
        pass

    def delete_user(self, value_dict):
        pass
