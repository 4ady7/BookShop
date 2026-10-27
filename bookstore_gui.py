import tkinter as tk
from tkinter import messagebox
from bookstore_core_inher import BookStore, Customer, Stock, Order, Shipping, Invoice
import datetime
from tkinter import ttk


class UserInterface:  
    def __init__(self): 
        self.bookstore = BookStore("Thank you for shopping with us! We hope to see you again.") #creating an instance of the class Bookstore, and naming it bookstore

        self.root = tk.Tk() #creating the main window 
        self.root.geometry("900x700") #specifing the width and the height, the width to 900, and the height to 700
        self.root.title("Book Ordering System") #naming the main window Book Ordering System

        self._customers = [] #creating a list and naming it customers to store each creaated customer
        self._stocks = [] #creating a list and naming it stocks to store each creaated book
        self._orders = [] #creating an order list, and naming it Orders
        self._current_order = None #the order waiting for shipping and an invoice
        self._current_shipping = None #the shipping record for the current order
        self.isUrgent = tk.BooleanVar(value=False)
        self.customer_var = tk.StringVar()
        self.book_var = tk.StringVar()


        searchButton = tk.Button(self.root, text="SearchID", command=self.searchBar, font=("Arial", 14), width=15) #creating a search button in the main window to be clicked by the user
        searchButton.pack(anchor="center", pady=10) #positioning the button in the center of the main window, and using pady to add space above and below 
        
        

        customerAddButton = tk.Button(self.root, text="Add Customer", command=self.customerInputForm, font=("Arial", 14), height=1, width=15) #creating an add customer button to be clicked by the user in the main window, and another window will pop up to add details for adding a customer 
        customerAddButton.pack(anchor="center", pady=10) #positioning the lablel in the center of the main window, and using pady to add space above and below 


        self.dropDown1 = ttk.Combobox(self.root, textvariable=self.customer_var, state="readonly", width=32) #creating a dropdown in the main window to allow the user to choose a created customer 
        self.dropDown1.pack(anchor="center") #positioning the dropdown in the center of the main window 



        self.labelTracker1 = tk.Label(self.root, text="No item selected") #creating a label in the main window to keep the user informed 
        self.labelTracker1.pack(anchor="center") #positioning the lablel in the center of the main window 




        bookAddButton = tk.Button(self.root, text="Add Book to Stock", command=self.bookInputForm, font=("Arial", 14), height=1, width=15) #creating an add book button to be clicked by the user in the main window, and another window will pop up to add details for adding a book
        bookAddButton.pack(anchor="center", pady=10) #positioning the lablel in the center of the main window, and using pady to add space above and below

        self.dropDown2 = ttk.Combobox(self.root, textvariable=self.book_var, state="readonly", width=32) #creating a dropdown in the main window to allow the user to choose a created book 
        self.dropDown2.pack(anchor="center") #positioning the dropdown in the center of the main window 




        self.labelTracker2 = tk.Label(self.root, text="No item selected") #creating a label in the main window to keep the user informed 
        self.labelTracker2.pack(anchor="center") #positioning the lablel in the center of the main window 


        self.placeOrderBbutton = tk.Button(self.root, text="Place the Order", command=self.orderPlacement, font=("Arial", 14), width=13) #creating an add book button to be clicked by the user in the main window, and is valid after the user has choosen a customer from the dropdown for the customer and choosen a book from the dropdowndown for books
        self.placeOrderBbutton.pack(anchor="center", pady=5) #positioning the dropdown in the center of the main window, and using pady to add space above and below

        




        shippingButton = tk.Button(self.root, text="Shipping Options", command=self.shippingOptions, font=("Arial", 14), height=1, width=15) #creating a button to be clicked by the user in the main window for calculating the shipping depending on wheather the user has checked the isUrgentCheckbox or not  
        shippingButton.pack(anchor="center", pady=10) #positioning the checkbox in the center of the main window, and using pady to add space above and below 
        

        invoiceGenerationButton = tk.Button(self.root, text="Invoice Generation", command=self.invoiceGeneration, font=("Arial", 14), width=13) #creating a button to be clicked by the user in the main window for generating an invoice to view the total cost and the invoice number 
        invoiceGenerationButton.pack(anchor="center", pady=5) #positioning the checkbox in the center of the main window, and using pady to add space above and below 


        viewAllInvoicesButton = tk.Button(self.root, text="View All Invoices", font=("Arial", 14), width=13, command=self.view_invoices) #creating a button to be clicked by the user in the main window for view all the previously generated invoices   
        viewAllInvoicesButton.pack(anchor="center", pady=5) #positioning the checkbox in the center of the main window, and using pady to add space above and below 

    def _clear_open_shipment(self):
        """Drop shipping for an order that has not been invoiced yet."""
        shipping = self._current_shipping
        if shipping is not None and shipping._counted_urgent:
            Shipping.count_urgent -= 1
            shipping._counted_urgent = False
        self._current_shipping = None



    """
    creating a window that pops up ontop of the main window to allow the user to place the order
    """
    def shippingOptions(self):
        self.selectShippingWindow = tk.Toplevel(self.root) #creating a window that pops up ontop of the main window to choose shipping
        self.selectShippingWindow.title("Shipping Options")
        """
        assigning the boolean value to the variable isUrgent
        if the value is ticked the value True is going to be assigned to the variable isUrgent
        and if the value is not ticked then the value Fasle is going to be assigned to the variable isUrgent
        """
        isUrgentCheckbox = tk.Checkbutton(self.selectShippingWindow, text="Is it an Urgent Order?", variable=self.isUrgent) #creating a checkbox for the shipping option to allow the user to tick it or leave it empty 
        isUrgentCheckbox.grid(row=3, column=0) #positioning the checkbox at row 3 and column 0 


        calculateShippingButton = tk.Button(self.selectShippingWindow, text="Calculate Shipping", command=self.calculateShipping) #creating a button to be clicked by the user in the window selectShippingWindow for calculating the shipping depending on wheather the user has checked the isUrgentCheckbox or not  
        calculateShippingButton.grid(row=5, column=0) #positioning the button at row 5 and column 0 

    
   
    """
    creating a window that pops up ontop of the main window to allow the user to search for an order by the invoice ID
    """
    def searchBar(self):
        self.searchWindow = tk.Toplevel(self.root) #creating a window that pops up ontop of the main window to allow the user to search for an order by the invoice ID
        self.searchWindow.title("Search by ID") #naming the pop up window Search by ID

        searchLabel = tk.Label(self.searchWindow, text="Search") #creating a label inside the pop window to clarify what the entry widget is for, and naming it Search
        searchLabel.grid(row=0, column=0) #positioning the label at row 0 and column 0 

        self.searchEntry = tk.Entry(self.searchWindow, font=("Arial", 25)) #creating an entry widget inside the pop window to allow the user to add an input to be searched for 
        self.searchEntry.grid(row=0, column=1) #positioning the entry widget at row 0 and column 1


        """
        creating the button
        """
        searchCommand = self.search #assigning the class function search to the variable searchCommand 
        searchButton = tk.Button(self.searchWindow, text="Search for an Invoice", command = searchCommand) #creating a button when clicked, the search for an invoice occurs.
        searchButton.grid(row=3, column=0, columnspan=2) #positioning the button at row 3 and column 2

    
    



    def customerInputForm(self):
        self.customerInputWindow = tk.Toplevel(self.root) #creating a window that pops up ontop of the main window to allow the user to enter the customer's details
        self.customerInputWindow.title("Add New Customer") #naming the pop up window Add New Customer

        # Customer form within the new window
        nameLabel = tk.Label(self.customerInputWindow, text="Name") #creating a label inside the pop window to clarify what the entry widget is for, and naming it Name refering to the Customer Name
        nameLabel.grid(row=0, column=0) #positioning the label at row 0 and column 0 

        self.nameEntry = tk.Entry(self.customerInputWindow) #creating an entry widget inside the pop window to allow the user to add an input to be saved as the Customer's Name 
        self.nameEntry.grid(row=0, column=1) #positioning the entry widget at row 0 and column 1

        phoneLabel = tk.Label(self.customerInputWindow, text="Phone") #creating a label inside the pop window to clarify what the entry widget is for, and naming it Phone refering to the Customer Phone Number
        phoneLabel.grid(row=1, column=0) #positioning the label at row 1 and column 0

        self.phoneEntry = tk.Entry(self.customerInputWindow) #creating an entry widget inside the pop window to allow the user to add an input to be saved as the customer's Phone Number 
        self.phoneEntry.grid(row=1, column=1) #positioning the entry widget at row 1 and column 1

        emailLabel = tk.Label(self.customerInputWindow, text="Email") #creating an entry widget inside the pop window to allow the user to add an input to be saved as the customer's email address 
        emailLabel.grid(row=2, column=0) #positioning the label at row 2 and column 0

        self.emailEntry = tk.Entry(self.customerInputWindow) #creating an entry widget inside the pop window to allow the user to add an input to be saved as the customer's email
        self.emailEntry.grid(row=2, column=1) #positioning the entry widget at row 2 and column 1
        

        """
        creating the button
        """
        customerCommand = self.addCustomer #assigning the class function addCustomer to the variable customerCommand 
        ConfirmInputButton = tk.Button(self.customerInputWindow, text="Confirm Customer details", command = customerCommand) #creating a button when clicked the customer is created
        ConfirmInputButton.grid(row=3, column=0, columnspan=2) #positioning the button at row 3 and column 2





     
    def addCustomer(self): 
        Name = self.nameEntry.get().strip() #getting the entry value of nameEntry and assigning it to the variable Name 
        Phone = self.phoneEntry.get().strip() #getting the entry value of phoneEntry and assigning it to the variable Phone  
        Email = self.emailEntry.get().strip() #getting the entry value of emailEntry and assigning it to the variable Email 

        try:
            customer = Customer(Name, Phone, Email) #validation runs in the Customer setters
        except (TypeError, ValueError) as error:
            messagebox.showerror("Error", str(error))
            return

        self._customers.append(customer) #add the created customer to the list customers 
        self.updatingCustomerDropDown() #call the function updatingCustomerDropDown
        """
        The updatingCustomerDropDown function is called to refresh the Combobox, so that when 
        the combobox is used, then the created customer/s that was added would appear ther in the combobox 
        """
        messagebox.showinfo("Success", f"Customer {Name} added!") #displaying a pop-up message, informing the user the customer has been successfully added 
        self.customerInputWindow.destroy() #closint the window for the customer input form



        
       
        """
        the function is used to refresh the Combobox, so tthat the new created customer value that was 
        added to the customers list would be displayed as the customer name in the dropdown for the user to make a choice 
        """
    def updatingCustomerDropDown(self):
        #creatingg a list and assigning it to the variable customerNames
        customerNames = []
        #looping through each customer in the customers list
        for customerInList in self._customers:
            #adding the name attribute of each customer in the customers list to the customerNames list
            customerNames.append(customerInList._name)
        #adding each customer name to dropdown by assigning the customerNames list to the customer dropdown widget values
        self.dropDown1["values"] = customerNames 




    def bookInputForm(self):
        self.add_book_window = tk.Toplevel(self.root) #creating a window that pops up ontop of the main window for the entry of the book details
        self.add_book_window.title("Add New Book") #naming the pop up window Add New Book

        bookNameLabel = tk.Label(self.add_book_window, text="Book Name") #creating a label inside the pop window to clarify what the entry widget is for, and naming it Book Name refering to the Book Name
        bookNameLabel.grid(row=0, column=0) #positioning the label at row 0 and column 0 

        self.bookNameEntry = tk.Entry(self.add_book_window)
        self.bookNameEntry.grid(row=0, column=1) #positioning the entry widget at row 0 and column 1

        authorLabel = tk.Label(self.add_book_window, text="Author")
        authorLabel.grid(row=1, column=0) #positioning the label at row 1 and column 0 

        self.authorEntry = tk.Entry(self.add_book_window)
        self.authorEntry.grid(row=1, column=1) #positioning the entry widget at row 1 and column 1 

        priceLabel = tk.Label(self.add_book_window, text="Price")
        priceLabel.grid(row=2, column=0) #positioning the label at row 2 and column 0 

        self.priceEntry = tk.Entry(self.add_book_window)
        self.priceEntry.grid(row=2, column=1) #positioning the entry widget at row 2 and column 1

        """
        creating the button
        """
        bookCommand = self.addBook #assigning the function add_book to the variable bookCommand
        ConfirmInputButton = tk.Button(self.add_book_window, text="Confirm Book details", command = bookCommand) #creating a button when clicked the book is created
        ConfirmInputButton.grid(row=3, column=0, columnspan=2) #positioning the button at row 3 and column 2

    

    def addBook(self):
        bookNamed = self.bookNameEntry.get().strip() #getting from the entry variable bookNameEntry, it's value, and assigning this valaue to the variable bookNamed
        author = self.authorEntry.get().strip() #getting from the entry variable authorEntry, it's value, and assigning this valaue to the variable author
        priced = self.priceEntry.get().strip() #getting from the entry variable priceEntry, it's value, and assigning this valaue to the variable priced
        try:
            stock = Stock(bookNamed, author, priced) #validation runs in the Stock setters
        except (TypeError, ValueError) as error:
            messagebox.showerror("Error", str(error))
            return
        self._stocks.append(stock) #add the created stock to the list stocks 
        self.updateStockDropDown() #call the function updateStockDropDown
        messagebox.showinfo("Success", f"Book {bookNamed} added!")
        """
        The updateStockDropDown function is called to refresh the dropdown, so that when 
        the dropdown is used, then the created stock/s that was added would appear in the dropdown 
        """
        self.add_book_window.destroy() #close the window for the stock input form









        """
        the function is used to refresh the Combobox, so tthat the new created customer value that was 
        added to the customers list would be displayed in the dropdown as the customer name for the user to make a choice 
        """
    def updateStockDropDown(self):
        BookNames = [] #creating a list and assigning it to the variable BookNames
        for stockInList in self._stocks: #looping through each stock(book) in the stocks list
            BookNames.append(stockInList._bookName) #adding the bookName attribute of each stock(book) in the stocks list to the BookNames list
        #adding each book name to dropdown by assigning the BookNames list to the stock dropdown widget values
        self.dropDown2["values"] = BookNames #assigning the BookNames list to the stock dropdown widget values


    
    """
    The order placement function is designed to create an order, using the most recent value of customer, and most recent value of stock
    The order placement function also sets the shipping cost depending on the tick or untick choice of the user for the urgent shipping 
    """
    def orderPlacement(self):
        customerNAme = self.dropDown1.get() #getting and assigning the selectetd customer from the dropdown to the variable selected_customer
        stockBookNAme = self.dropDown2.get() #getting and assigning the selected stock from the dropdown to the variable selected_customer
        
        """Searching for a customer"""
        customer = None #assigning the variable customer to None 
        for CUSTOMER in self._customers: #iterating through the list of customers 
            if CUSTOMER._name == customerNAme: #if the selected customer name is found in the list of customers, then perform the following.
                customer = CUSTOMER #assign the value of the selection to the variable customer 
                self.labelTracker1.config(text="Thanks for selecting an option") #overwriting the labeltracker for the customer dropdown, informing the user that he has made an option when the place the order button is clicked 
                break #exitting the for loop once the customer selected is found

        
        """searching for a stock"""
        stock = None #assigning the variable stock to None 
        for STOCK in self._stocks: #iterating through the list of customers 
            if STOCK._bookName == stockBookNAme: #if the selected book name is found in the list of stocks, then perform the following.
                stock = STOCK #assign the value of the selection to the variable stock 
                self.labelTracker2.config(text="Thanks for selecting an option") #overwrite the labeltracker for the stock dropdown, informing the user that he has made an option when the place the order button is clicked 
                break #exitting the for loop once the book selected is found

        
            
        if not customer: #in case the variable customer is empty and still assigned to None, then perform the following:
            self.labelTracker1.config(text="go back and select an item from the customer list!") #overwriting the labeltracker for the customer dropdown, informing the user that a choice needs to be made for the customer dropdown 
            
        
        if not stock: #in case the variable stock is empty and still assigned to None, then perform the following:
            self.labelTracker2.config(text="go back and select an item from the stock list!") #overwriting the labeltracker for the stock dropdown, informing the user that a choice needs to be made for the stock dropdown 
            
            
        if customer and stock:
            if self._current_order is not None:
                self._clear_open_shipment()
                if self._current_order in self._orders:
                    self._orders.remove(self._current_order)
            order = Order(customer, stock) #creating an order of customer and stock, and adding it to the list
            self._orders.append(order) #adding an order to the orders list each time an order is placed by pressing the order placement button
            self._current_order = order
            messagebox.showinfo("Order Placed", f"Order has been successfully placed for {customerNAme} for the purchase of {stockBookNAme}. Choose shipping options next.") #displaying a message informing the user that they have succefullyy placed the order, and the messagebox also displays the customer name and the book name 






    def calculateShipping(self):
        urgentShipping = self.isUrgent.get() #using the getter to get the boolean value of the variable isUrgent

        if self._current_order is None:
            messagebox.showwarning("Error", "Place an order before calculating shipping.")
            return

        if self._current_shipping is None:
            self._current_shipping = Shipping(self._current_order, datetime.date.today())
        shippingCOst = self._current_shipping.calc_ship_cost(urgentShipping) #£5.45 when urgent, otherwise £3.95, stored on this shipment
        stock = self._current_order._stock
        totalCost = float(stock._price) + float(shippingCOst)
        messagebox.showinfo("Shipping Calculated", f"Shipping is £{float(shippingCOst):.2f}. Total price for {stock._bookName} is £{totalCost:.2f} including shipping.")
        self.selectShippingWindow.destroy() #closing the shippping options window
        

        

        



    """
"""

    def search(self):
        entryNUM = self.searchEntry.get().strip() #assigning the inputted ID by the user to the variable entryNUM

        if not entryNUM: #if the user is clicking the search button before enterring an invoice ID, the following messagebox will be displayed 
            messagebox.showinfo("Error", "There seems to be no invoice ID entered by user") #displaying a pop-up message, informing the user there was no invoice number inputed
            return

        results = self.bookstore.search_invoice(entryNUM) #search the invoice repository
        if not results:
            messagebox.showerror("Result not found", "The invoice number that you are looking for is nowhere to be found, please check your number and try again. For reference: INV0001. Make sure to capitalize your letters.")
            return
        everyINVOICE = results[0]
        messagebox.showinfo("Result found", f"{everyINVOICE}") #the messagebox shows the invoice, including shipping
        self.searchWindow.destroy() #closing the search window


        

    def invoiceGeneration(self): 
        if self._current_order is None:
            messagebox.showwarning("Error", "Place an order before generating an invoice.")
            return
        if self._current_shipping is None:
            messagebox.showwarning("Error", "Calculate shipping before generating an invoice.")
            return

        order = self._current_order
        shipping = self._current_shipping
        invoice_number = f"INV{len(self.bookstore.invoices) + 1:04d}" 
        """
        the f string takes the string INV and the string value inside the curcly braces, 
        and then the string value of f sting is assigned to the variable invoice_number 
        using the len() method to count how many invoice are in the invoices list,
        the curly braces take the integer value of the number of values inside the list, 
        and incremented by 1, and as I am specifying the it has to be a four digit number, 
        so if it is less than one thousand(1000), the rest will be filled withinvoice zero as instance: 0999 or 0013
        """

        invoice = Invoice(invoice_number, order._stock, shipping) #the invoice uses the order that was placed and the shipping cost already calculated
        self.bookstore.invoices.append(invoice) #adding an invoice to the invoices list each time a valid the invoice generation is called by pressing the invoice generation button
        messagebox.showinfo(
            "Generation of an Invoice",
            f"An invoice {invoice_number} has been successfully generated.\nShipping: £{float(shipping._ship_cost):.2f}\nTotal Cost: £{invoice.invoice():.2f}",
        )
        self._current_order = None
        self._current_shipping = None
        self.isUrgent.set(False)




        

    def view_invoices(self):
        if not self.bookstore.invoices: #if the invoices list is empty then do the following: 
            messagebox.showinfo("Not found", "There is no invoice available in the invoices list") #displaying a pop-up message, informing the user there was no invoice found in the invoices list 
            return

        allInvoices = "\n\n".join(str(everyInvoice) for everyInvoice in self.bookstore.invoices)
        messagebox.showinfo("All Invoices", allInvoices) #displaying a pop-up message to the screen that displays the invoices with details: an invoice number and the total cost
            


if __name__ == "__main__":
    #calling the main funtion
    userInterface = UserInterface()
    userInterface.root.mainloop()