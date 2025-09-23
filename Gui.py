import tkinter as tk
from tkinter import messagebox

expenses = []

def add_expense():
    name = entry_name.get()
    try:
        money = int(entry_money.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a number for money!")
        return

    expenses.append((name, money))
    messagebox.showinfo("Added", f"{name} - {money} 💰")
    entry_name.delete(0, tk.END)
    entry_money.delete(0, tk.END)
    show_expenses()

def show_expenses():
    listbox.delete(0, tk.END)
    for name, money in expenses:
        listbox.insert(tk.END, f"{name} : {money} 💵")

def sort_expenses():
    # Bubble sort
    for i in range(len(expenses)):
        for j in range(0, len(expenses) - i - 1):
            if expenses[j][1] > expenses[j+1][1]:
                expenses[j], expenses[j+1] = expenses[j+1], expenses[j]
    show_expenses()

def total_expenses():
    total = sum([m for _, m in expenses])
    if total > 1000:
        messagebox.showwarning("Total", f"💡 Total: {total} 💰\n😱 Whoa! You spent a lot!")
    else:
        messagebox.showinfo("Total", f"💡 Total: {total} 💰\n🤑 Nice! You are saving money!")

# Main window
root = tk.Tk()
root.title("Expense Tracker with FUN + Bubble Sort 🎉")
root.geometry("400x400")

# Input fields
tk.Label(root, text="What did you buy?").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="How much money?").pack()
entry_money = tk.Entry(root)
entry_money.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=5)
tk.Button(root, text="View Expenses", command=show_expenses).pack(pady=5)
tk.Button(root, text="Sort (Bubble Sort)", command=sort_expenses).pack(pady=5)
tk.Button(root, text="Total Spent", command=total_expenses).pack(pady=5)

# Listbox for showing expenses
listbox = tk.Listbox(root, width=40)
listbox.pack(pady=10)

# Run the GUI
root.mainloop()
