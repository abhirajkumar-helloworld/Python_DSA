Queue = []

while True:
    print("------------------------")
    print("1. Join Queue")
    print("2. Serve Customer")
    print("3. Show first Customer")
    print("4. exit")

    choice = input("Enter your choice : ")

    if choice == "4":
        print("Exiting.....")
        break

    elif choice == "1":
        join_queue = input("Join Queue : ")
        Queue.append(join_queue)
        print(f"{join_queue} joined")

    elif choice == "2":
        if len(Queue) == 0:
            print("No Customer to served")

        else:
            print(f"{Queue.pop(0)} has been served")
            if len(Queue) == 0:
                print("No customer to served")

            else:
                print(f"Current Customer : {Queue[0]}")

    elif choice == "3":
        if len(Queue) == 0:
            print("No Customer to served")

        else:
            print(f"First Customer : {Queue[0]}")

    else:
        print("Enter the choice from the above list")