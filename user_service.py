from main.database.user_sql import UserDB
class UserService:
    def __init__(self):
        self.userdb=UserDB()


    def open_account(self):
        print("welcome to user account open page")
        print()
        first_name=input("please enter first name: ")
        last_name = input("please enter last name:")
        dob=input("please enter date of birth:")
        gender=input("please enter gender(male/female):")
        aadhar=int(input("please enter aadhar:"))
        pan=input("please enter pan number:")
        account_balance=float(input("please enter initial account balance :"))
        ifsc_code=input("please enter ifsc_code:")
        address=input("please enter address:")
        pincode=int(input("please enter pincode:"))

        input_dict={}
        input_dict["first_name"]=first_name
        input_dict["last_name"] = last_name
        input_dict["dob"] = dob
        input_dict["gender"] = gender
        input_dict["aadhar"] = aadhar
        input_dict["pan"] = pan
        input_dict["account_balance"] = account_balance
        input_dict["ifsc_code"] = ifsc_code
        input_dict["address"] = address
        input_dict["pincode"] = pincode

        print("input from user in dictionary:")
        print(input_dict)

        self.userdb.insert_new_user(input_dict)


