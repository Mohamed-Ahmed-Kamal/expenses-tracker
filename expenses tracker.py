import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ExpensesTracker:
    def __init__(self, window):
        self.window = window
        self.window["bg"] = "#4f639f"
        self.window.title("Expenses Tracker")

        self.expenses = []
        self.total_expenses = tk.DoubleVar()

        self.label_amount = tk.Label(window, text="Amount =>")
        self.entry_amount = tk.Entry(window)
        self.label_category = tk.Label(window, text="Category =>")
        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(window, textvariable=self.category_var,
                                              values=["Alimony", "Life Expenses", "Electricity", "Gas",
                                                      "Rental", "Grocery", "Savings", "Education", "Charity"])
        self.label_date = tk.Label(window, text="Date =>")
        self.entry_date = tk.Entry(window)
        self.label_payment_method = tk.Label(window, text="Payment Method =>")
        self.payment_method_var = tk.StringVar()
        self.payment_method_combobox = ttk.Combobox(window, textvariable=self.payment_method_var,
                                                    values=["Cash", "Credit Card", "Paypal"])
        self.label_currency = tk.Label(window, text="Currency =>")
        self.currency_var = tk.StringVar()
        self.currency_combobox = ttk.Combobox(window, textvariable=self.currency_var,
                                              values=["EGP", "USD", "EUR"])
        self.button_add = tk.Button(
            window, text="Add Expense", command=self.add_expense)
        self.button_add["bg"] = "green"

        self.treeview = ttk.Treeview(window, columns=(
            "ID", "Amount", "Currency", "Category", "Date", "Payment Method"), show="headings")
        self.treeview.heading("ID", text="ID")
        self.treeview.heading("Amount", text="Amount")
        self.treeview.heading("Currency", text="Currency")
        self.treeview.heading("Category", text="Category")
        self.treeview.heading("Date", text="Date")
        self.treeview.heading("Payment Method", text="Payment Method")
        self.treeview.column("ID", width=40, anchor=tk.CENTER)
        self.treeview.column("Amount", width=80, anchor=tk.E)
        self.treeview.column("Currency", width=80, anchor=tk.CENTER)
        self.treeview.column("Category", width=100, anchor=tk.CENTER)
        self.treeview.column("Date", width=100, anchor=tk.CENTER)
        self.treeview.column("Payment Method", width=100, anchor=tk.CENTER)

        self.treeview.insert("", "end", iid="Total", values=(
            "Total", "", "", "", "", ""), tags=('total',))

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(
            'TkDefaultFont', 10, 'bold'))
        self.style.configure("Treeview", font=('TkDefaultFont', 9))

        self.label_amount.grid(row=0, column=0, padx=10, pady=10)
        self.entry_amount.grid(row=0, column=1, padx=10, pady=10)
        self.label_category.grid(row=2, column=0, padx=10, pady=10)
        self.category_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.label_date.grid(row=3, column=0, padx=10, pady=10)
        self.entry_date.grid(row=3, column=1, padx=10, pady=10)
        self.label_payment_method.grid(row=4, column=0, padx=10, pady=10)
        self.payment_method_combobox.grid(row=4, column=1, padx=10, pady=10)
        self.label_currency.grid(row=5, column=0, padx=10, pady=10)
        self.currency_combobox.grid(row=5, column=1, padx=10, pady=10)
        self.button_add.grid(row=6, column=0, columnspan=2, pady=10)
        self.treeview.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_expense(self):
        amount = self.entry_amount.get()
        category = self.category_var.get()
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        payment_method = self.payment_method_var.get()
        currency = self.currency_var.get()

        try:
            amount = float(amount)
            self.expenses.append(
                (amount, currency, category, date, payment_method))

            row_id = len(self.expenses)
            self.treeview.insert("", "end", iid=row_id, values=(
                row_id, f"${amount:.2f}", currency, category, date, payment_method))

            self.total_expenses.set(
                sum(expense[0] for expense in self.expenses))

            self.update_total_row()

            self.entry_amount.delete(0, tk.END)
            self.category_combobox.set("")
            self.entry_date.delete(0, tk.END)
            self.entry_date.insert(0, date)
            self.payment_method_combobox.set("")
            self.currency_combobox.set("")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def update_total_row(self):
        total_amount = self.total_expenses.get()
        self.treeview.item("Total", values=(
            "Total", f"${total_amount:.2f}", "", "", "", ""), tags=('total',))
        self.treeview.tag_configure('total', background='yellow')


if __name__ == "__main__":
    window = tk.Tk()
    app = ExpensesTracker(window)
    window.mainloop()
