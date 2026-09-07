'''
Hotel Menu using Dictionary and conditional statements
'''
menu = {
    "Burger": 60,
    "Pizza": 120,
    "Pasta": 40,
    "Salad": 30,
    "Sandwich": 50,
    "Juice": 20,
    "Coffee": 25,
    "Tea": 20,
    "Ice-Cream": 25,
    "Shwarma": 80,
    "Pastry": 35
}
#Greeting the customer
print("Welcome to our Fast Food Restaurant!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: Rs {price}")
order_total = 0
while True:
    user_order = input("Please enter the item you want to order and its quantity or type 'done' to finish your order: ")
    if user_order == "done":
        break
    try:
        item, quantity = user_order.split()
        quantity = int(quantity)
        if item in menu:
            order_total += menu[item] * quantity
        else:
            print("Sorry, we don't have that item on the menu.")
    except ValueError:
        print("Invalid input. Please enter the item and quantity separated by a space.")
        
print(f"Your total order amount is: Rs {order_total}")