page = []

while True:
    print("-------------------------------")
    print("1. Visit page")
    print("2. Back")
    print("3. Current page")
    print("4. Exit")

    choice = input("Enter your choice : ")

    if choice == "4":
        print("Exiting....")
        break

    elif choice == "1":
        a = input("Enter page : ")
        page.append(a)

    elif choice == "2":
        if len(page) == 0:
            print("No page in history")

        else:
            page.pop()
            print("Backed")
            if len(page) == 0:
                print("No page in history")
            else:
                print(f"Current page : {page[-1]}")

    elif choice == "3":
        if len(page) == 0:
            print("No Pages in history")

        else:
            print(f"Current page : {page[-1]}")

    else:
        print("Enter the choice from the above list")