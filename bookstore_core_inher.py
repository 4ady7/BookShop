"""
The following Person class is going to represent a person with
a name, a phone number, and an email

(name, phone, email) -> str
name: the person's name 
phone: the person's phone number 
email: the person's email address 
"""
class Person: #creating the person class
    def __init__(self, name: str, phone: str, email: str): #the __init__ function takes 3 attributes, and all of them are string attributes 
        self._name = name #creating a variable that can be passed into an object of the class
        self._phone = phone #creating a variable that can be passed into an object of the class
        self._email = email #creating a variable that can be passed into an object of the class


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
The following Customer class inherits the attributies: name, phone, and email from the class Person

The Customer class is going to represent a customer with
a name, a phone number, and an email

(name, phone, email) -> str
name: the customer's name 
phone: the customer's phone number 
email: the customer's email address 
"""
class Customer(Person): #creating the Customer class 
    def __init__(self, name: str, phone: str, email: str):
        #inheriting the attributies: name, phone, and email from the class Person
        Person.__init__(self, name, phone, email)

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
        self._bookName = book_name #creating a variable that can be passed into an object of the class
        self._price = price #creating a variable that can be passed into an object of the class

    
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
        checking if validPrice is a float
        if it is not then raise an error 
        """
        if not isinstance(validPrice, float):
            raise TypeError("You should enter a decimal number") #adjusting it to two decimal place because in most stores it is common to have prices that look like this 7.55 like this 7.90 or 7.50 or 1.50
        """
        ensuring that validPrice is not less than 
        if it is less then raise an error 
        """
        if validPrice < 0:
            raise ValueError("The price have to be more than 0")
        """
        checking if the length of validPrice is betwween 4 and 15
        if not then raise an error
        """
        if not 4 <= len(str(validPrice)) <= 15:
            raise ValueError("price length needs to be adjusted")
        """
        adjusting it to two decimal place because in most stores it is common to have prices that look like this 7.56
        if it more than 2 decimal places then raisse an error 
        """
        if len(str(validPrice).split('.')[1]) < 2: 
            raise ValueError("The price should only include tenths and hundredths places") 
        #removing every empty space 
        validPrice = str(validPrice).replace(" ","")
        """
        ensuring that validPrice has exactly one dot  
        if it does not then raise an error 
        """
        if str(validPrice).count(".") != 1:
            raise TypeError("You might have forgot to add a dot or added more than one dot")

        print("Calling the price setter...")
        self._price = validPrice



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
The following Stock class inherits the attributies: book name, and price from the class Product

The Stock class is going to represent a stock with
a book Name and a price

(bookName, author) -> str
(price) --> Double float
bookName: the name of the book
price: the price of the product
"""
class Stock: #creating the Customer class 
    def __init__(self, bookName: str, author: str, price: float):
        #inheriting the attributies: bookName, and email from the class Person
        Product.__init__(self, bookName, price)
        self._author = author #creating a variable that can be passed into an object of the class

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
        checking if validPrice is a float
        if it is not then raise an error 
        """
        if not isinstance(validPrice, float):
            raise TypeError("You should enter a decimal number") #adjusting it to two decimal place because in most stores it is common to have prices that look like this 7.55 like this 7.90 or 7.50 or 1.50
        """
        ensuring that validPrice is not less than 
        if it is less then raise an error 
        """
        if validPrice < 0:
            raise ValueError("The price have to be more than 0")
        """
        checking if the length of validPrice is betwween 4 and 15
        if not then raise an error
        """
        if not 4 <= len(str(validPrice)) <= 15:
            raise ValueError("price length needs to be adjusted")
        """
        adjusting it to two decimal place because in most stores it is common to have prices that look like this 7.56
        if it more than 2 decimal places then raisse an error 
        """
        if len(str(validPrice).split('.')[1]) < 2: 
            raise ValueError("The price should only include tenths and hundredths places") 
        #removing every empty space 
        validPrice = str(validPrice).replace(" ","")
        """
        ensuring that validPrice has exactly one dot  
        if it does not then raise an error 
        """
        if str(validPrice).count(".") != 1:
            raise TypeError("You might have forgot to add a dot or added more than one dot")

        print("Calling the price setter...")
        self._price = validPrice



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


    BookName = property(getbookName, setbookName) #creating the property method for the book name
    Price = property(getprice, setprice) #creating the property method for the price of the stock 
    Author = property(getauthor, setauthor) #creating the property method for the author name



class Order:
    def __init__(self, customer, stock):
        self._customer = customer
        self._stock = stock

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
        if self._customer is None:
            print("Value has not been set yet.")
            return None
        self._customer = validcustomer

    
    def setstock(self, validstock):
        print("Calling the self._stock setter...")
        if self._stock is None:
            print("Value has not been set yet.")
            return None
        self._stock = validstock

        

import datetime 
class Shipping:
    count_urgent = 0 #craeting a variable inside the class and initializing it, so that it equals to zero
    
    def __init__(self, order, ship_date):
        self._order = order
        self.ship_date = ship_date
        self._ship_cost = 0.00 #instantiating the shipping cost as a float 
    
    #creating a method of the class that calculates the shipping cost depending on the time of delivery
    def calc_ship_cost(self, is_urgent: bool):
        #using if statement so that if shipping is urgent return 5.45 and if shipping is not urgent then return 3.95 
        if is_urgent == True:
            #incrementing the count_urgent by 1 each time is_urgent is equal to True
            Shipping.count_urgent += 1
        #returning a different price depending on the cost of the shipping
            return 5.45 #if True
        else:
            return 3.95 #if False

    def get_ship_cost(self):
        #Calling the ship_cost getter...
        return self._ship_cost

    def set_ship_cost(self, validShipCost):
        if self._ship_cost is None:
            print("Value has not been set yet.")
            return None
        #Calling the ship_cost setter...
        self._ship_cost = validShipCost

    shippingCost = property(get_ship_cost, set_ship_cost) #creating the property method for the shipping cost  


    @property
    def order(self):
        #Calling the order getter...
        return self._order
    
    @order.setter
    def order(self, validOrder):
        if self._order is None:
            print("Value has not been set yet.")
            return None
        #Calling the order setter...
        print(f"setting order to {validOrder}")
        self._order = validOrder


    @property
    def ship_date(self):
        #Calling the ship_date getter..."
        return self._ship_date
    
    @ship_date.setter
    def ship_date(self, validShipDate):
        validShipDate = datetime.date.today()
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
    
    #creating a method of the class that calculates the total cost, which is the summation of the price and shipping cost
    def invoice(self):
        #returning the summation of the follwoing equation, which takes the price and the shipping cost to get the total cost
        total_cost = self.stock._price + self.ship_order._ship_cost
        return total_cost
    
    
    @property
    def get_invoice_nbr(self):
        #Calling the invoice_nbr getter...
        return self._invoice_nbr
    
    @property
    def get_total_cost(self):
        #Calling the total_cost getter...
        return self.total_cost
    
    @property
    def get_ship_order(self):
        #Calling the ship_order getter...
        return self.ship_order

    
 
class BookStore:
    #the __init__ function that takes the final message, and instantiating the the invoices as a list 
    def __init__(self, message: str):
        self.message = message
        self._invoices = []

    #Creating a method to allow searching for an invoice by an invoice number
    def search_invoice(self, searchInput):
        #creating a list and assigning it to the variable results 
        results = [] 
        #creatingg a loop that loops through every invoice in the invoices list
        for inv in self._invoices:
            #if the entered invoice number by the user matches one of the invoice numbers of the invoices in the list of invoices, then append the invoice in the invoices list to the results list 
            if searchInput in inv._invoice_nbr:
                #appending the invoice in the invoices list to the results list 
                results.append(inv)
        """
        checking if results is not empty 
        if the results list is not empty then for the invoice in the results list, print it in the terminal below using the following print(invoice)
        if the results list is empty then using the print statement, display no results found
        """
        #checking if results is not empty    
        if results:
            for invoice in results: 
                print(invoice) 
        else:
            print("no results found")

    @property 
    def invoices(self):
        #Calling the invoices getter...
        return self._invoices


class Test:
    def main():

        try:
            nameOfCustomer = str(input("Enter the name of the customer: ")).strip() #taking an input from the user and assigning it to the variable nameOfCustomer
            if not isinstance(nameOfCustomer, str): #checking if nameOfCustomer is a string
                print("A name should be written as a string") #if not then print
                #nameOfCustomer = str(input("Enter the name of the customer: ")).strip() #if we want to stop the programm until the user adds a correct customer name format, we can this line of code asking the user to input the name again after explaining to the user what went wrong
            validNameInputs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .'-èéüçñabcdefghijklmnopqrstuvwxyz"
            """
            checking if every letter in nameOfCustomer is inisde validNameInputs
            if not then print 
            """
            for letter in nameOfCustomer: 
                if letter not in validNameInputs: #ensuring that each character in nameOfCustomer is is not outside validNameInputs
                    print("A name should consist of alphabetical letters and somtimes if needed some special characters") #if it is outside then print
                    #nameOfCustomer = str(input("Enter the name of the customer: ")).strip() #if we want to stop the programm until the user adds a correct customer name format, we can this line of code asking the user to input the name again after explaining to the user what went wrong
            if not 3 <= len(nameOfCustomer) <= 30: #checking if the length of nameOfCustomer is betwween 3 and 30
                print("A name should be between 3 and 30 character") #if not then print
                #nameOfCustomer = str(input("Enter the name of the customer: ")).strip() #if we want to stop the programm until the user adds a correct customer name format, we can this line of code asking the user to input the name again after explaining to the user what went wrong
        except Exception: #if there is an exception then print
            print("Please, Enter the customer name again") #informing the user to enter the input again 

        try:
            phoneOfCustomer = str(input("Enter the phone number of the customer: ")).strip() #taking an input from the user and assigning it to the variable phoneOfCustomer
            if not isinstance(phoneOfCustomer, str): #checking if phoneNumber is a string
                print("A phone number should be written as a string") #if it is not then print 
            if not len(phoneOfCustomer) == 11: #checking if phoneOfCustomer is an 11 digit number 
                print("A phone number should be written as 11 digit phone number") #if it is not then print 
            if not phoneOfCustomer.startswith("07"): #checking if phoneOfCustomer starts with 07 
                print("A phone number should be written as a phone number that starts with 07") #if it is not then print 
            for character in phoneOfCustomer:
                if not character.isdigit(): #ensuring that each character in phoneOfCustomer is a digit 
                    print("A phone number should be written as digits only") #if it is not then print 
        except Exception: #if there is an exception then print
            print("Please, Enter the customer phone number again") #informing the user to enter the input again 


        try:
            emailOfCustomer = str(input("Enter the email address of the customer: ")).strip() #taking an input from the user and assigning it to the variable emailOfCustomer
            if not isinstance(emailOfCustomer, str): #checking if emailOfCustomer is a string
                print("An email address should be written as a string") #if it is not then print 
            if not 5 <= len(emailOfCustomer) <= 250: #checking if the length of validEmailAddress is betwween 5 and 250
                    print("An email address should be written between 5 and 250 character") #if it is not then print 
            if emailOfCustomer.count("@") != 1: #checking if validEmailAddress is written with exactly one @(At sign)
                print("An email address should be written with exactly one @(At sign). So you might have forgot to add @ or add more than one @") #if it is not then print 
            if emailOfCustomer.count(".") != 1: #checking if validEmailAddress is written with exactly one dot
                print("An email address should be written with exactly one dot. So you might have forgot to add a dot or add more than one a dot") #if it is not then print 
            emailOfCustomer = emailOfCustomer.strip() #the strip() method is used for the benefit of the user by aiding in removing the leading spaces if there were any at the beginning of the sentence. It is also used to remove trailing spaces if there were any at the end of the sentence. 
            emailOfCustomer = emailOfCustomer.replace(" ","") #the replace() method is used for the benefit of the user by aiding in removing the spaces in the middle between words. So in case the user has added a space by mistake, the program is going to automatically remove it without raising an error.  
            validEmailInputs = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@0123456789."
            """
            checking if every letter in emailOfCustomer is inisde validEmailInputs
            if not then print 
            """
            for char in emailOfCustomer:
                if char not in validEmailInputs: #ensuring that each character in emailOfCustomer is not outside validEmailInputs
                    print("An email address should only include alphabetical letters, numbers, a @(At sign) and a dot.") #if it is outside then print 
        except Exception: #if there is an exception then print
            print("Please, Enter the customer phone number again") #informing the user to enter the input again 


        """
        Inputs that raise no error 
        Enter the name of the customer: Adam Fisher
        Enter the phone number of the customer: 07123456789
        Enter the email address of the customer: adamFisher@gmail.com
        """
        customer1 = Customer(nameOfCustomer, phoneOfCustomer, emailOfCustomer) #creating an instance of the customer class that takes its parameters as inputs from the user 
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

 
 
if __name__ == "__main__": #the entry point for the program exceution 
    Test.main() #calling the main method