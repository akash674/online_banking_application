from main.services.user_service import UserService

if __name__ == '__main__':
    print("starting the service")
    user_service=UserService()
    user_service.open_account()

    print("ending the service")


from main.services.transaction_service import TransactionService

if __name__ == '__main__':
    print("starting the service")
    transaction_service=TransactionService()
    transaction_service.create_transaction_id()
    print("ending the service")"""



