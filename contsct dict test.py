import json

phone_book = {}

try:
    with open("contact.json", "r") as file:
        phone_book = json.load(file)        
except:
    pass

while True:
    print("1: add num")
    print("2: view num")
    print("3: search num")
    print("4: remove num")
    print("5: exit")

    choice = input("enter your choice: ").strip()

    if choice == '1':
        name = input("enter your name: ").strip().title()
        number = input("enter your phone number: ").strip()

        if number in phone_book.values():
            print("number already exists...")
        else:
           phone_book[name] = number
           print("contact added")

    elif choice == '2':
        if len(phone_book) == 0:
            print("no numbers added yet...")
        else:
            for name in phone_book:
                print(name, ":", phone_book[name])

    elif choice == '3':
        search = input("enter your name to be found: ").strip().title()
        if search in phone_book:
            print("found!!")
            print("number: ", phone_book[search])
        else:
            print("not found...")
    
    elif choice == '4':
        remove = input("enter a name to be removed: ").strip().title()
        if remove in phone_book:
            del phone_book[remove]
            print("removed")
        else:
            print("not found")

    elif choice == '5':
        with open("contact.json", "w") as file:
            json.dump(phone_book, file)
            print("saved sucessfully!!!")
            break

    else:
        print("invalid choice")
#test complete.....