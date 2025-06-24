import tkinter as tk
from tkinter import messagebox

class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):
        if not self.items:
            return "No items in order."
        summary = "Your Order:\n"
        for i, item in enumerate(self.items, 1):
            summary += f"{i}. {item.name} - ${item.price}\n"
        summary += f"\nTotal: ${self.total()}"
        return summary

    def clear(self):
        self.items.clear()

# --- GUI Part ---

def add_to_order(coffee):
    order.add_item(coffee)
    messagebox.showinfo("Item Added", f"{coffee.name} added to your order.")

def view_order():
    summary = order.show_order()
    messagebox.showinfo("Order Summary", summary)

def checkout():
    if not order.items:
        messagebox.showwarning("Empty Cart", "Your cart is empty.")
        return

    summary = order.show_order()
    confirm = messagebox.askyesno("Confirm Checkout", summary + "\n\nProceed to checkout?")
    if confirm:
        messagebox.showinfo("Order Confirmed", "Order confirmed! Thank you.")
        order.clear()
    else:
        messagebox.showinfo("Checkout Cancelled", "Checkout cancelled.")

def exit_app():
    root.destroy()

# Main Window
root = tk.Tk()
root.title("Coffee Shop")
root.geometry("600x600")

# Order and Menu
order = Order()
menu = [
    Coffee("Espresso", 2.5),
    Coffee("Latte", 3.5),
    Coffee("Cappuccino", 3.0),
    Coffee("Americano", 2.0)
]

# GUI Layout
tk.Label(root, text="Welcome to the Coffee Shop!", font=("Helvetica", 16)).pack(pady=10)

menu_frame = tk.Frame(root)
menu_frame.pack(pady=10)

for coffee in menu:
    btn = tk.Button(menu_frame, text=f"{coffee.name} - ${coffee.price}", width=30, command=lambda c=coffee: add_to_order(c))
    btn.pack(pady=5)

action_frame = tk.Frame(root)
action_frame.pack(pady=20)

# Stylish font and button color settings
button_style = {
    "bg": "black",
    "fg": "white",
    "font": ("Comic Sans MS", 12, "bold"),
    "width": 15,
    "padx": 5,
    "pady": 5
}

# Action Buttons with new styles
tk.Button(action_frame, text="View Order", command=view_order, **button_style).pack(side="left", padx=10)
tk.Button(action_frame, text="Checkout", command=checkout, **button_style).pack(side="left", padx=10)
tk.Button(root, text="Exit", command=exit_app, **button_style).pack(pady=10)

# Run the App
root.mainloop()
