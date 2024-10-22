print("Welcome to Taco Palace! Please view the menu below and make a selection")
print()

def menu():
    print("Taco Palace Menu")
    print("0.Taco $2.00")
    print("1.Burrito $5.00")
    print("2.Nachos $3.00")
    print("3.Soft Drink $6.00")
    print("4.Quit Menu")

menu()

total_amount = 0.0
orders = []
menu_items = int(input("Select an option\n"))

def foodMenu(index):
    menu = ["Tacos","Burrito","Nachos","Soft Drink","Quit Menu"]
    return menu[index]

while(menu_items >= 0):
    if menu_items < 4:
        item = foodMenu(menu_items)
        print("You have selected",item)
        orders.append(item)
        prices = [2.00, 5.00, 3.00,6.00]
        total_amount += prices[menu_items]
        print("$",total_amount)
        menu()
    elif menu_items == 4:
        print('Thanks for your order!')
        break
    else:
        print('Select a number from 0 to 4')
    print()
    menu_items = int(input("Select an option\n"))

if orders:
    print("You ordered:\n")
    for order in orders:
        print(order)
    print("Your total amount due: ${:.2f}".format(total_amount))
else:
    print("Nothing selected")
