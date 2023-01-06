from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from tkcalendar import DateEntry

import logic_layer


class MainWindow:

    def __init__(self, master, admin_view):
        self.root = master
        self.admin_view = admin_view
        self.statusMessage = StringVar()
        # Create and grid the outer content frame
        self.mainPanel = ttk.Frame(self.root, padding=(5, 5, 12, 0))
        self.mainPanel.grid(column=0, row=0, sticky="nsew")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Creating widgets
        self.catalog = ttk.Treeview(self.mainPanel, columns=('title', 'author'), height=5, show='headings',
                                    selectmode='extended')
        self.catalog.heading('title', text='Title')
        self.catalog.heading('author', text='Author')
        self.catalogLabel = ttk.Label(self.mainPanel, text="Catalog", anchor='center')

        self.cart = ttk.Treeview(self.mainPanel, columns=('title', 'author'), height=5, show='headings',
                                 selectmode='extended')
        self.cart.heading('title', text='Title')
        self.cart.heading('author', text='Author')
        self.cartLabel = ttk.Label(self.mainPanel, text="Cart", anchor='center')

        self.addToCart = ttk.Button(self.mainPanel, text='Add to Cart', command=self.add_to_cart, default='active')
        self.refresh = ttk.Button(self.mainPanel, text='Refresh', command=self.build_catalog, default='active')
        self.removeFromCart = ttk.Button(self.mainPanel, text='Remove from Cart', command=self.remove_from_cart,
                                         default='active')
        self.lendBooks = ttk.Button(self.mainPanel, text='Lend Books', command=self.lend_books, default='active')

        self.pickupDateSelect = DateEntry(self.mainPanel, dateformat='y-mm-dd')
        self.pickupDateLabel = ttk.Label(self.mainPanel, text="Choose book pick-up date:")
        self.returnDateSelect = DateEntry(self.mainPanel, dateformat='y-mm-dd')
        self.returnDateLabel = ttk.Label(self.mainPanel, text="Choose book return date:")

        self.description = Text(self.mainPanel, state='disabled')

        self.lbl = ttk.Label(self.mainPanel, text="henlo")
        self.status = ttk.Label(self.mainPanel, textvariable=self.statusMessage, anchor=W)

        # Grid all the widgets
        self.catalog.grid(column=0, row=1, rowspan=6, columnspan=3, sticky="nswe")
        self.catalogLabel.grid(column=1, row=0, pady=6)
        self.cart.grid(column=6, row=1, rowspan=6, columnspan=3, sticky="nswe")
        self.cartLabel.grid(column=7, row=0, pady=6)

        self.addToCart.grid(column=1, row=8, sticky="we")
        self.refresh.grid(column=2, row=8, sticky="we")
        self.removeFromCart.grid(column=7, row=8, sticky="we")
        self.lendBooks.grid(column=8, row=8, sticky="we")

        self.pickupDateSelect.grid(column=11, row=2, pady=10, sticky="nswe")
        self.pickupDateLabel.grid(column=11, row=1, sticky="s")
        self.returnDateSelect.grid(column=11, row=4, pady=10, sticky="nswe")
        self.returnDateLabel.grid(column=11, row=3, sticky="s")

        self.description.grid(column=0, row=9, columnspan=9, sticky="nswe")

        self.lbl.grid(column=4, row=0, padx=10, pady=5)
        self.status.grid(column=0, row=10, columnspan=2, sticky="we")
        self.mainPanel.grid_columnconfigure(0, weight=1)
        self.mainPanel.grid_columnconfigure(1, weight=1)
        self.mainPanel.grid_columnconfigure(2, weight=1)
        self.mainPanel.grid_columnconfigure(6, weight=1)
        self.mainPanel.grid_columnconfigure(7, weight=1)
        self.mainPanel.grid_columnconfigure(8, weight=1)
        # mainPanel.grid_rowconfigure(5, weight=1)

        # Set event bindings for when the selection in the listbox changes
        self.catalog.bind('<<TreeviewSelect>>', self.show_details)

        self.catalog.selection_clear()
        self.build_catalog()

    def add_to_cart(self):
        nodes = self.catalog.selection()
        for node in nodes:
            book = self.catalog.item(node, option='values')
            book_id = self.catalog.item(node, option='text')
            self.cart.insert('', 'end', id=node, text=book_id, values=(book[0], book[1]))

    def remove_from_cart(self):
        nodes = self.cart.selection()
        for node in nodes:
            self.cart.delete(node)

    def build_catalog(self):
        nodes = self.catalog.get_children('')
        for node in nodes:
            self.catalog.delete(node)
            if self.cart.exists(node):
                self.cart.delete(node)

        data = logic_layer.get_catalog()

        for (book_id, title, author) in data:
            self.catalog.insert('', 'end', text=book_id, values=(title, author))

    def lend_books(self):
        books = self.cart.get_children('')
        book_ids = list()
        for book in books:
            book_ids.append(self.cart.item(book, option='text'))
        try:
            logic_layer.lend_book(book_ids, self.pickupDateSelect.get_date(), self.returnDateSelect.get_date())
        except ValueError:
            messagebox.showerror(message="One or more books are already lent out in selected time period.")
# Called when the selection in the listbox changes

    def show_details(self, *args):
        nodes = self.catalog.selection()
        if len(nodes) >= 1:
            last_id = nodes[len(nodes) - 1]
            pk = self.catalog.item(last_id, option='text')
        # get details from database
        # display details


# show_details()

if __name__ == "__main__":
    root = Tk()
    root.title("Biblioteca")
    MainWindow(root)
    root.mainloop()
