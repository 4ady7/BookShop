"""
The following Person class is going to represent a person with
a name, a phone number, and an email

(name, phone, email) -> str
name: the person's name 
phone: the person's phone number 
email: the person's email address 
"""

import datetime
import re
from decimal import Decimal


def _parse_price(validPrice):
    """Return a price as a float with at most two decimal places."""
    if isinstance(validPrice, str):
        text = validPrice.strip().replace(" ", "")
        if not re.fullmatch(r"\d+(\.\d{1,2})?", text):
            raise ValueError("The price should only include tenths and hundredths places")
        amount = Decimal(text)
    elif isinstance(validPrice, bool) or not isinstance(validPrice, (int, float)):
        raise TypeError("You should enter a decimal number")
    else:
        amount = Decimal(str(validPrice))
        rounded = amount.quantize(Decimal("0.01"))
        if abs(amount - rounded) > Decimal("0.0000001"):
            raise ValueError("The price should only include tenths and hundredths places")
        amount = rounded
    if amount <= 0:
        raise ValueError("The price have to be more than 0")
    return float(amount.quantize(Decimal("0.01")))


class Person: #creating the person class
    def __init__(self, name: str, phone: str, email: str): #the __init__ function takes 3 attributes, and all of them are string attributes 
        self.Name = name
        self.Phone = phone
        self.Email = email


    """
The following access the attributes of the person and returns 
them when called using getters for each attribute 
for example:
person10 = Person("Jakey", "07456789123", "Jakey@gmail.com")
person10.getemail() #the output will be: Jakey@gmail.com
    """
    def getname(self):
        """
        returning the person name
        (person name --> str)
        """
        return self._name

    
    def getphone(self): 
        """
        returning the person phone number
        (person phone number --> str)
        """
        return self._phone
    
    def getemail(self):
        """
        returning the person email address
        (person email address --> str)
        """
        return self._email 
    
    def setName(self, validName):
        if not isinstance(validName, str):
            raise TypeError("You need to add quotes before and after the name, because names must be written as a string")
        validNameInputs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .'-èéüçñabcdefghijklmnopqrstuvwxyz"
        for letter in validName:
            if letter not in validNameInputs:
                raise ValueError("You can only enter alphabetical letters and some special characters")
        if not 3 <= len(validName) <= 30:
            raise ValueError("Please enter a name between 3 and 30 character")
        
        print("Calling the name setter...")     
        self._name = validName #assigning the value to the private attribute (_name) inside the setter, without triggering the setter itself again. The private attribute (_name) stores the actual value, and the setter is just used for validation. I am doing that to avoid an infinite recersion that leads to RecursionError.

    
    def setPhone(self, phoneNumber):
        if not isinstance(phoneNumber, str):
            raise TypeError("You need to add quotes before and after the Phone number, because phone numbers must be written as a string")
        if not len(phoneNumber) == 11:
            raise ValueError("Please enter an 11 digit phone number")
        if not phoneNumber.startswith("07"):
            raise ValueError("phonenumber must start with 07")
        for character in phoneNumber:
            if not character.isdigit():
                raise ValueError("You can only enter numbers")
                   
        print("Calling the phone setter...")
        self._phone = phoneNumber


    def setEmail(self, validEmailAddress):
        if not isinstance(validEmailAddress, str):
            raise TypeError("You need to add quotes before and after the email address, because email addresses must be written as a string")
        if not 5 <= len(validEmailAddress) <= 250:
                raise ValueError("Please enter an email address between 5 and 250 character")
        if validEmailAddress.count("@") != 1:
            raise TypeError("You might have forgot to add @ or add more than one @")
        if validEmailAddress.count(".") != 1:
            raise TypeError("You might have forgot to add a dot or add more than one a dot")
        validEmailAddress = validEmailAddress.strip() #the strip() method is used for the benefit of the user by aiding in removing the leading spaces if there were any at the beginning of the sentence. It is also used to remove trailing spaces if there were any at the end of the sentence. 
        validEmailAddress = validEmailAddress.replace(" ","") #the replace() method is used for the benefit of the user by aiding in removing the spaces in the middle between words. So in case the user has added a space by mistake, the program is going to automatically remove it without raising an error.  
        validEmailInputs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@0123456789."
        for char in validEmailAddress:
            if char not in validEmailInputs:
                raise ValueError("You can only enter alphabetical letters, numbers, a @, and a dot.")
        
        print("Calling the email setter...")
        self._email = validEmailAddress


    Name = property(getname, setName)
    Phone = property(getphone, setPhone)
    Email = property(getemail, setEmail)








"""
The following Customer class inherits name, phone, and email from Person.
A customer is a person who orders books.
"""
class Customer(Person):
    def __init__(self, name: str, phone: str, email: str):
        super().__init__(name, phone, email)



"""
The following Product class is going to represent a customer with
a book Name, an author name, and a price

(bookName, author) -> str
(price) --> Double float
bookName: the name of the book
author: the name of the author
price: the price of the product
"""
class Product:
    #the __init__ function takes 3 attributes (2 of them are strings, and one is a float variable)
    def __init__(self, book_name: str, price: float):
        self.BookName = book_name
        self.Price = price

    
        """
The following access the attributes of the stock and returns 
them when called using getters for each attribute 
for example:
stock10 = Stock("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 11.46)
stock10.getauthor() #the output will be: C.S. Lewis
    """
    def getbookName(self):
        """
        returning the bookName in the Stock class
        (stock bookName --> str)
        """
        return self._bookName.strip() 
    """
    strip() method is used to remove leading spaces if there 
    were any at the beginning of the book name. It is also used to 
    remove trailing spaces if there were any at the end of the book name
    """


    
    def getprice(self):
        """
        returning the price in the Stock class
        (stock price --> str)
        """
        return self._price
    

    def setprice(self, validPrice):
        """
        Store the book price as a float with at most two decimal places.
        """
        print("Calling the price setter...")
        self._price = _parse_price(validPrice)


    def setbookName(self, validBookName):
        """
        checking if validBookName is a string
        if it is not then raise an error 
        """
        if not isinstance(validBookName, str): 
            raise TypeError("You need to add quotes before and after the book name, because book name must be written as a string")
        validBookNameInputs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ' -.abcdefghijklmnopqrstuvwxyz1234567890"
        """
        checking if every letter in validBookName is inisde validBookNameInputs
        if not then raise an error 
        """
        for letter in validBookName: 
            if letter not in validBookNameInputs:
                raise ValueError("You can only enter alphabetical letters, numbers, spaces, hyphens, dots, and apostrophes.")
            """
            checking if the length of validBookName is betwween 3 and 150
            if not then raise an error
            """
        if not 3 <= len(validBookName) <= 150:
            raise ValueError("Please enter a book name between 3 and 150 character")
        print("Calling the book_name setter...")
        self._bookName = validBookName #assigning the value to the private attribute (book_name) inside the setter, without triggering the setter itself again. The private attribute (book_name) stores the actual value, and the setter is just used for validation. I am doing that to avoid an infinite recersion that leads to RecursionError.





    BookName = property(getbookName, setbookName) #creating the property method for the book name
    Price = property(getprice, setprice) #creating the property method for the price of the stock 
    

    


"""
The Stock class inherits book name and price from Product and adds the author.
"""
class Stock(Product):
    def __init__(self, bookName: str, author: str, price: float):
        super().__init__(bookName, price)
        self.Author = author

    def getauthor(self): 
        """
        returning the author in the Stock class
        (stock author --> str)
        """
        return self._author.strip()
    """
    strip() method is used to remove leading spaces if there 
    were any at the beginning of the book name. It is also used to 
    remove trailing spaces if there were any at the end of the book name
    """

    
    def setauthor(self, validAuthor):
        if not isinstance(validAuthor, str):
            raise TypeError("You need to add quotes before and after the name, because names must be written as a string")
        validAuthorNameInputs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .'-èéüçñabcdefghijklmnopqrstuvwxyz"
        for letter in validAuthor:
            if letter not in validAuthorNameInputs:
                raise ValueError("You can only enter alphabetical letters and some special characters")
        if not 3 <= len(validAuthor) <= 30:
            raise ValueError("Please enter a name between 3 and 30 character")
        print("Calling the author setter...")
        self._author = validAuthor #assigning the value to the private attribute (_author) inside the setter, without triggering the setter itself again. The private attribute (_author) stores the actual value, and the setter is just used for validation. I am doing that to avoid an infinite recersion that leads to RecursionError.


    Author = property(getauthor, setauthor) #creating the property method for the author name


class Order:
    def __init__(self, customer, stock):
        self.setcustomer(customer)
        self.setstock(stock)

    """
The following access the attributes of the order and returns 
them when called using getters for each attribute 
for example:
order10 = Order(customer10, stock10)
    """
    def getcustomer(self):
        print("Calling the self._customer getter...")
        return self._customer
    
    def getstock(self):
        print("Calling the self._stock getter...")
        return self._stock
    
    def setcustomer(self, validcustomer):
        print("Calling the self._customer setter...")
        if not isinstance(validcustomer, Customer):
            raise TypeError("Order customer must be a Customer")
        self._customer = validcustomer

    
    def setstock(self, validstock):
        print("Calling the self._stock setter...")
        if not isinstance(validstock, Stock):
            raise TypeError("Order stock must be a Stock item")
        self._stock = validstock


class Shipping:
    count_urgent = 0 #craeting a variable inside the class and initializing it, so that it equals to zero
    
    def __init__(self, order, ship_date):
        self._ship_cost = 0.00 #instantiating the shipping cost as a float
        self._counted_urgent = False
        self.order = order
        self.ship_date = ship_date
    
    #creating a method of the class that calculates the shipping cost depending on the time of delivery
    def calc_ship_cost(self, is_urgent: bool):
        #using if statement so that if shipping is urgent return 5.45 and if shipping is not urgent then return 3.95
        #count_urgent tracks shipments, so changing the same shipment does not count it twice
        if is_urgent == True:
            if not self._counted_urgent:
                Shipping.count_urgent += 1
                self._counted_urgent = True
            self._ship_cost = 5.45
            return self._ship_cost
        if self._counted_urgent:
            Shipping.count_urgent -= 1
            self._counted_urgent = False
        self._ship_cost = 3.95
        return self._ship_cost

    def get_ship_cost(self):
        #Calling the ship_cost getter...
        return self._ship_cost

    def set_ship_cost(self, validShipCost):
        if isinstance(validShipCost, bool) or not isinstance(validShipCost, (int, float)):
            raise TypeError("Shipping cost must be a number")
        if validShipCost < 0:
            raise ValueError("Shipping cost cannot be negative")
        #Calling the ship_cost setter...
        self._ship_cost = float(validShipCost)

    shippingCost = property(get_ship_cost, set_ship_cost) #creating the property method for the shipping cost  


    @property
    def order(self):
        #Calling the order getter...
        return self._order
    
    @order.setter
    def order(self, validOrder):
        if not isinstance(validOrder, Order):
            raise TypeError("Shipping order must be an Order")
        #Calling the order setter...
        print(f"setting order to {validOrder}")
        self._order = validOrder


    @property
    def ship_date(self):
        #Calling the ship_date getter..."
        return self._ship_date
    
    @ship_date.setter
    def ship_date(self, validShipDate):
        if not isinstance(validShipDate, datetime.date):
            raise TypeError("Ship date must be a date")
        #Calling the ship_date setter...
        print(f"setting ship_date to {validShipDate}")
        self._ship_date = validShipDate







class Invoice:
    #the __init__ function takes a variable and 2 objects of previously created classes(the stock class and the shipping class)
    def __init__(self, invoice_nbr: str, stock: Stock, ship_order: Shipping):
        self._invoice_nbr = invoice_nbr
        self.stock = stock
        self.ship_order = ship_order
        self.total_cost = 0.00 #instantiating the total cost as a float 
    
    """
    creating a method of the class that calculates the total cost, which is the summation of the price and shipping cost
    """
    def invoice(self):
        self.total_cost = float(self.stock._price) + float(self.ship_order._ship_cost)
        return self.total_cost

    def __str__(self):
        total = self.invoice()
        customer = self.ship_order._order._customer
        return (
            f"Invoice {self._invoice_nbr}: {customer._name}, "
            f"{self.stock._bookName} by {self.stock._author}, "
            f"book £{float(self.stock._price):.2f}, "
            f"shipping £{float(self.ship_order._ship_cost):.2f}, "
            f"total £{total:.2f}"
        )
    
    
    @property
    def get_invoice_nbr(self):
        #Calling the invoice_nbr getter...
        return self._invoice_nbr
    
    @property
    def get_total_cost(self):
        #Calling the total_cost getter...
        return self.invoice()
    
    @property
    def get_ship_order(self):
        #Calling the ship_order getter...
        return self.ship_order

    
 
class BookStore:
    #the __init__ function that takes the final message, and instantiating the the invoices as a list 
    def __init__(self, message: str):
        self.message = message
        self._invoices = [] #creating an invoices list 

    """
    Creating a method to allow searching for an invoice by an invoice number
    creating a list and assigning it to the variable results 
    creating a loop that loops through every invoice in the invoices list
    if the entered invoice number by the user matches one of the invoice numbers of the invoices in the list of invoices, then append the invoice in the invoices list to the results list
    appending the invoice in the invoices list to the results list  
    """
    def search_invoice(self, searchInput): #Creating a method to allow searching for an invoice by an invoice number
        results = [] #creating a list and assigning it to the variable results 
        for inv in self._invoices: #creatingg a loop that loops through every invoice in the invoices list
            if inv._invoice_nbr == searchInput: #exact invoice number match
                results.append(inv) #appending the invoice in the invoices list to the results list
        """
        checking if results is not empty 
        if the results list is not empty then for the invoice in the results list, print it in the terminal below using the following print(invoice)
        if the results list is empty then using the print statement, display no results found
        """
        #checking if results is not empty    
        if results: #if results is not empty do the following loop through results list and print the invoice in the list 
            for invoice in results: #loop through results list
                print(invoice) #print the invoice in the list 
        else: #if the results list is empty then print the following
            print("no results found") #displaying and informing the user that no result has been found
        return results

    @property 
    def invoices(self):
        #Calling the invoices getter...
        return self._invoices


class Test:
    @staticmethod
    def main():
        """
        Inputs that raise no error
        Enter the name of the customer: Adam Fisher
        Enter the phone number of the customer: 07123456789
        Enter the email address of the customer: adamFisher@gmail.com
        """
        while True:
            try:
                nameOfCustomer = input("Enter the name of the customer: ").strip()
                phoneOfCustomer = input("Enter the phone number of the customer: ").strip()
                emailOfCustomer = input("Enter the email address of the customer: ").strip()
                customer1 = Customer(nameOfCustomer, phoneOfCustomer, emailOfCustomer)
                break
            except (TypeError, ValueError) as error:
                print(error)
                print("Please enter the customer details again")
        customer2 = Customer("Tyler Hoverman", "07456789123", "TylerHoverman@gmail.com") #creating an instance of the customer class
        customer3 = Customer("Mason Green", "07123456789", "MasonGreen@gmail.com") #creating an instance of the customer class

 
        stock1 = Stock("Prince Caspian", "C.S. Lewis", 5.78) #creating an instance of the stock class
        stock2 = Stock("Winning the War on Worry", "Louie Giglio", 12.29) #creating an instance of the stock class
        stock3 = Stock("Think Ahead" , "Craig Groeschel", 12.55) #creating an instance of the stock class
 
 
        order1 = Order(customer1, stock1) #creating an instance of the order class
        order2 = Order(customer2, stock2) #creating an instance of the order class
        order3 = Order(customer3, stock3) #creating an instance of the order class
 
 
        shipping1 = Shipping(order1, datetime.date.today()) #creating an instance of the shipping class
        shipping2 = Shipping(order2, datetime.date.today()) #creating an instance of the shipping class
        shipping3 = Shipping(order3, datetime.date.today()) #creating an instance of the shipping class
        
 
        shipping1.set_ship_cost(shipping1.calc_ship_cost(True)) #setting the shipping option to urgent shipping, which costs 5.45.
        shipping2.set_ship_cost(shipping2.calc_ship_cost(False)) #setting the shipping option to a NOT urgent shipping, which costs 3.95.
        shipping3.set_ship_cost(shipping3.calc_ship_cost(True)) #setting the shipping option to urgent shipping, which costs 5.45.
 
 
        invoice1 = Invoice("INV0001", stock1, shipping1) #creating an instance of the invoice class
        invoice2 = Invoice("INV0002", stock2, shipping2) #creating an instance of the invoice class
        invoice3 = Invoice("INV0003", stock3, shipping3) #creating an instance of the invoice class
 
 
        bookstore = BookStore("Thank you for shopping with us! We hope to see you again.") #creating an instance of the BookStore class
 
        bookstore.invoices.append(invoice1) #adding invoice1 to the list of invoices
        bookstore.invoices.append(invoice2) #adding invoice2 to the list of invoices
        bookstore.invoices.append(invoice3) #adding invoice3 to the list of invoices
 
        print(f"Number of urgent shipments: {shipping1.count_urgent}") #displaying the value of count_urgent, which is the number of urgent shippings
        print(f"Invoice 1 total cost: {invoice1.invoice():.2f}") #displaying the total cost for invoice1 with two decimal places 
        print(f"Invoice 2 total cost: {invoice2.invoice():.2f}") #displaying the total cost for invoice2 with two decimal places
        print(f"Invoice 3 total cost: {invoice3.invoice():.2f}") #displaying the total cost for invoice3 with two decimal places
 
        bookstore.search_invoice("INV0004") #searching for a non-existent invoice, and so it will display no result found

        print(bookstore.message) #displayig the final message 

 
 
if __name__ == "__main__":
    #calling the main method
    Test.main() 