# assignment
# atm ko balance widthdraw garni pin rakhera ani balance pani check gana milni     


balance = 5000
pin = 1234

user_pin = int(input("Enter your 4-digit PIN: "))

if user_pin == pin:
    choice = int(input("Enter 1 to check balance and 2 to withdraw money: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal successful.")
            print("Remaining balance is:", balance)
        else:
            print("Insufficient balance.")

    else:
        print("Invalid choice.")

else:
    print("Incorrect PIN. Access denied.")
    
    
# output:
# Enter your 4-digit PIN: 1234
# Enter 1 to check balance and 2 to withdraw money: 1
# Your balance is: 5000        

# Enter your 4-digit PIN: 1234
# Enter 1 to check balance and 2 to withdraw money: 2
# Enter the amount to withdraw: 5000
# Withdrawal successful.
# Remaining balance is: 0

# Enter your 4-digit PIN: 1223
# Incorrect PIN. Access denied.