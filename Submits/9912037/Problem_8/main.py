from bank import BankManagementSystemClass

bank_system_instance = BankManagementSystemClass()

while True:
    print("\nBank Management System")
    print("1. Create User")
    print("2. Create Account")
    print("3. Card-to-Card Transfer")
    print("4. SHABA Transfer")
    print("5. Check Balance")
    print("6. End Day")
    print("7. Account Info")
    print("8. Exit")

    user_choice_input = input("Enter your choice: ")

    if user_choice_input == "1":
        user_name = input("Enter user name: ")
        phone_number = input("Enter phone number: ")
        national_id = input("Enter national ID: ")

        if bank_system_instance.create_user_method(user_name, phone_number, national_id):
            print("User " + user_name + " registered successfully!")
        else:
            print("Registration failed! Invalid information.")

    elif user_choice_input == "2":
        user_name = input("Enter user name: ")
        account_type = input("Enter account type (Normal/ShortTerm/LongTerm): ")
        card_number = input("Enter card number: ")

        if bank_system_instance.create_account_method(user_name, account_type, card_number):
            print("Account created successfully!")
        else:
            print("Account creation failed!")

    elif user_choice_input == "3":
        sender_card = input("Enter sender card number: ")
        receiver_card = input("Enter receiver card number: ")
        amount = float(input("Enter amount: "))

        if bank_system_instance.transfer_card_to_card_method(sender_card, receiver_card, amount):
            print("Card-to-card transfer completed successfully!")
        else:
            print("Transfer failed!")

    elif user_choice_input == "4":
        sender_shaba = input("Enter sender SHABA number: ")
        receiver_shaba = input("Enter receiver SHABA number: ")
        amount = float(input("Enter amount: "))

        if bank_system_instance.transfer_shaba_method(sender_shaba, receiver_shaba, amount):
            print("SHABA transfer registered and will be completed at the end of the day.")
        else:
            print("Transfer failed!")

    elif user_choice_input == "5":
        card_number = input("Enter card number: ")
        balance = bank_system_instance.check_balance_method(card_number)
        if balance is not None:
            print("Balance of account " + card_number + ": " + str(balance) + " Tomans")
        else:
            print("Account not found!")

    elif user_choice_input == "6":
        result = bank_system_instance.process_end_of_day_method()
        print("End of day:")
        print(result)

    elif user_choice_input == "7":
        user_name = input("Enter user name: ")
        info = bank_system_instance.get_account_info_method(user_name)
        if info is not None:
            print(info)
        else:
            print("User not found!")

    elif user_choice_input == "8":
        break

    else:
        print("Invalid choice!")