balance = 1000
pin = "1234"

while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("0. Exit")
    
    choice = input("Select option: ")
    
    if choice == '1':
        print(f"Balance: {balance}")
    elif choice == '2':
        amount = int(input("Enter amount: "))
        balance += amount
    elif choice == '3':
        amount = int(input("Enter amount: "))
        if amount <= balance:
            balance -= amount
        else:
            print("No funds")
    elif choice == '4':
        print(f"Your PIN is: {pin}")
    elif choice == '5':
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print("PIN changed.")
        else:
            print("Invalid PIN.")
    elif choice == '0':
        break