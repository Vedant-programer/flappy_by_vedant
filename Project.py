# Self Order Service
# Python Project



print("WELCOME TO SELF ORDER")

print("Today's Menu")
print("1. Burger       - Rs. 80")
print("2. Pizza        - Rs. 120")
print("3. Sandwich     - Rs. 60")
print("4. French Fries - Rs. 50")
print("5. Cold Drink   - Rs. 40")
print("6. Pasta        - Rs. 90")


# prices of food items
burger = 80
pizza = 120
sandwich = 60
fries = 50
cold_drink = 40
Pasta=90

total = 0
order = []


while True:

    choice = input("Enter the item number (1-6): ")

    if choice == "1":
        item = "Burger"
        price = burger

    elif choice == "2":
        item = "Pizza"
        price = pizza

    elif choice == "3":
        item = "Sandwich"
        price = sandwich

    elif choice == "4":
        item = "French Fries"
        price = fries

    elif choice == "5":
        item = "Cold Drink"
        price = cold_drink
        
    elif choice== "6":
        item= "Pasta"
        price= Pasta

    else:
        print("Sorry, please enter a number between 1 and 6.")
        continue


    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    total = total + amount

    order.append([item, quantity, amount])

    print(item, "added to your order.")
    print("Amount:", amount)


    more = input("Do you want to order anything else? (yes/no): ")

    if more.lower() == "no":
        break


# GST calculation
gst = total * 2.3 / 100
final_amount = total + gst


# Printing bill

print("YOUR BILL")

for x in order:
    print(x[0], "x", x[1], "=", "Rs.", x[2])

print("Food Total : Rs.", total)
print("GST (2.3%)   : Rs.", gst)


print("TOTAL BILL : Rs.", final_amount)

print("******************************")

print("Thank you for using Self Order Service!")

print("Have a nice day!")
