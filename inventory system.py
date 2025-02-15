inventory = {}

while True:
    print("\n1. Add/Update Item")
    print("2. Get Item Info")
    print("3. View Total Quantity")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == '1':
        name = input("Taiyu shoes: ")
        quantity = int(input("10: "))
        inventory[name] = inventory.get(name, 0) + quantity
        print(f"{name} updated. Current quantity: {inventory[name]}.")

    elif choice == '2':
        name = input("Block shoes,Flat shoes: ")
        if name in inventory:
            print(f"{name}: {inventory[name]} units.")
        else:
            print(f"{name} not found.")

    elif choice == '3':
        total = sum(inventory.values())
        print(f"Total quantity: {total} units.")

    elif choice == '4':
        print("Exiting.")
        break

    else:
        print("Invalid choice. Please try again.")
