import random

bag = [random.randint(1,1000) for _ in range(5) ]

def display_bag(): 
    print("The items in your bag are:")
    print(bag)

def addtobag(item):
    bag.append(item)
    print("Item has been added to bag.")

def removefrombag(item):
    if item in bag:
        if len(bag)>5:
            bag.remove(item)
            print("Item removed.")
        elif len(bag)==5:
            print("Cannot remove as minimum amount of items is reached.")
    else:
        print("Item not in bag.")


while True:
    action = input("\nEnter 'add' to add items to the bag, 'remove' to remove items and 'exit' to display bag and exit ").strip().lower() 
    if action == "exit":
        display_bag()
        print("Exiting the program")
        break
    elif action == "add":
        display_bag()
        itemtobeadded = int(input("Enter the number of your item "))
        addtobag(itemtobeadded)
    elif action == "remove":
        display_bag()
        itemtoberemoved = int(input("Enter the number of the item you want to remove "))
        removefrombag(itemtoberemoved)
        display_bag()
    else:
        print("Invalid command, please try again.")



    

    

