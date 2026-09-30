# Self Order Service
# Python Project
# First Year Engineering Project

import tkinter as tk
from tkinter import messagebox
import random


# MAIN WINDOW 

window = tk.Tk()
window.title("Self Order Service")
window.geometry("1080x729")
window.resizable(False, False)

# FOOD MENU 

menu = {
    "Burger": 80,
    "Pizza": 120,
    "Sandwich": 60,
    "French Fries": 50,
    "Cold Drink": 40
}

total = 0
order_list = []


# FUNCTIONS

def add_order():

    global total

    item = food_choice.get()

    if item == "Select Food":
        messagebox.showwarning("Warning", "Please select a food item")
        return

    quantity = quantity_entry.get()

    if quantity == "":
        messagebox.showwarning("Warning", "Please enter quantity")
        return

    try:
        quantity = int(quantity)

        if quantity <= 0:
            messagebox.showwarning("Warning", "Quantity must be greater than 0")
            return

    except:
        messagebox.showwarning("Warning", "Please enter a number")
        return

    price = menu[item]
    amount = price * quantity

    total = total + amount

    order_list.append([item, quantity, amount])

    # Show order in bill box
    bill_box.insert(
        tk.END,
        item + " x " + str(quantity) + " = Rs. " + str(amount) + "\n"
    )

    total_label.config(text="Subtotal: Rs. " + str(total))

    quantity_entry.delete(0, tk.END)


def place_order():

    if len(order_list) == 0:
        messagebox.showwarning("Warning", "Please add something to your order")
        return

    gst = total * 5 / 100
    final_amount = total + gst

    order_number = random.randint(1000, 9999)

    bill_box.insert(tk.END, "\n--------------------------\n")
    bill_box.insert(tk.END, "GST (5%) = Rs. " + str(gst) + "\n")
    bill_box.insert(tk.END, "TOTAL = Rs. " + str(final_amount) + "\n")
    bill_box.insert(tk.END, "Order No. = " + str(order_number) + "\n")
    bill_box.insert(tk.END, "--------------------------\n")

    messagebox.showinfo(
        "Order Confirmed",
        "Your order has been placed!\n\n"
        "Order Number: " + str(order_number) +
        "\nTotal Amount: Rs. " + str(final_amount)
    )


def clear_order():

    global total

    total = 0
    order_list.clear()

    bill_box.delete("1.0", tk.END)

    total_label.config(text="Subtotal: Rs. 0")

    food_choice.set("Select Food")

    quantity_entry.delete(0, tk.END)


# ---------------- TITLE ----------------

title = tk.Label(
    window,
    text="SELF ORDER SERVICE",
    font=("Arial", 24, "bold")
)

title.pack(pady=15)


subtitle = tk.Label(
    window,
    text="Welcome! Select your food and place your order",
    font=("Arial", 11)
)

subtitle.pack()


# ---------------- LEFT SIDE ----------------

left_frame = tk.Frame(window)
left_frame.place(x=40, y=110, width=300, height=430)


menu_title = tk.Label(
    left_frame,
    text="Food Menu",
    font=("Arial", 18, "bold")
)

menu_title.pack(pady=10)


# Food prices

menu_text = """
Burger          Rs. 80
Pizza           Rs. 120
Sandwich        Rs. 60
French Fries    Rs. 50
Cold Drink      Rs. 40
"""

menu_label = tk.Label(
    left_frame,
    text=menu_text,
    font=("Arial", 12),
    justify="left"
)

menu_label.pack(pady=10)


# Food selection

food_label = tk.Label(
    left_frame,
    text="Select Food:",
    font=("Arial", 11)
)

food_label.pack(pady=5)


food_choice = tk.StringVar()
food_choice.set("Select Food")


food_menu = tk.OptionMenu(
    left_frame,
    food_choice,
    *menu.keys()
)

food_menu.config(width=18)

food_menu.pack()


# Quantity

quantity_label = tk.Label(
    left_frame,
    text="Enter Quantity:",
    font=("Arial", 11)
)

quantity_label.pack(pady=8)


quantity_entry = tk.Entry(
    left_frame,
    width=20
)

quantity_entry.pack()


# Add button

add_button = tk.Button(
    left_frame,
    text="ADD TO ORDER",
    command=add_order,
    width=20
)

add_button.pack(pady=15)


# RIGHT SIDE 

right_frame = tk.Frame(window)
right_frame.place(x=390, y=110, width=320, height=430)


order_title = tk.Label(
    right_frame,
    text="Your Order",
    font=("Arial", 18, "bold")
)

order_title.pack(pady=10)


# Bill box

bill_box = tk.Text(
    right_frame,
    width=35,
    height=14
)

bill_box.pack()


# Total

total_label = tk.Label(
    right_frame,
    text="Subtotal: Rs. 0",
    font=("Arial", 13, "bold")
)

total_label.pack(pady=8)


# Buttons

place_button = tk.Button(
    right_frame,
    text="PLACE ORDER",
    command=place_order,
    width=15
)

place_button.pack(side="left", padx=10)


clear_button = tk.Button(
    right_frame,
    text="CLEAR",
    command=clear_order,
    width=15
)

clear_button.pack(side="right", padx=10)


# FOOTER 

footer = tk.Label(
    window,
    text="Thank you for using Self Order Service!",
    font=("Arial", 10)
)

footer.pack(side="bottom", pady=10)


# START PROGRAM 

window.mainloop()