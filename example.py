"""
Example: Adam Fisher buys Prince Caspian with urgent shipping.

Book price £5.78 + urgent shipping £5.45 = invoice total £11.23.
The invoice is stored as INV0001 and can be found by that number.
"""

import bookstore_gui as gui


def show(title, message):
    print(f"[{title}] {message}")


gui.messagebox.showinfo = show
gui.messagebox.showerror = show
gui.messagebox.showwarning = show


def fill(entry, text):
    entry.delete(0, "end")
    entry.insert(0, text)


def main():
    gui.Shipping.count_urgent = 0
    window = gui.UserInterface()
    window.root.withdraw()

    window.customerInputForm()
    fill(window.nameEntry, "Adam Fisher")
    fill(window.phoneEntry, "07123456789")
    fill(window.emailEntry, "adamFisher@gmail.com")
    window.addCustomer()

    window.bookInputForm()
    fill(window.bookNameEntry, "Prince Caspian")
    fill(window.authorEntry, "C.S. Lewis")
    fill(window.priceEntry, "5.78")
    window.addBook()

    window.dropDown1.set("Adam Fisher")
    window.dropDown2.set("Prince Caspian")
    window.orderPlacement()

    window.isUrgent.set(True)
    window.shippingOptions()
    window.calculateShipping()

    window.invoiceGeneration()

    invoice = window.bookstore.invoices[0]
    total = invoice.invoice()
    print(f"Stored invoice: {invoice}")
    print(f"Urgent shipments: {gui.Shipping.count_urgent}")

    window.searchBar()
    fill(window.searchEntry, "INV0004")
    window.search()

    window.searchBar()
    fill(window.searchEntry, "INV0001")
    window.search()

    window.view_invoices()

    if len(window.bookstore.invoices) != 1:
        raise SystemExit("Expected one invoice in the repository")
    if invoice._invoice_nbr != "INV0001":
        raise SystemExit(f"Expected INV0001, got {invoice._invoice_nbr}")
    if abs(total - 11.23) > 0.001:
        raise SystemExit(f"Expected total 11.23, got {total:.2f}")
    if abs(invoice.ship_order._ship_cost - 5.45) > 0.001:
        raise SystemExit("Expected urgent shipping of 5.45")
    if gui.Shipping.count_urgent != 1:
        raise SystemExit(f"Expected 1 urgent shipment, got {gui.Shipping.count_urgent}")
    if invoice.ship_order._order is not window._orders[0]:
        raise SystemExit("Invoice shipping is not the order that was placed")

    print("Example passed.")
    window.root.destroy()


if __name__ == "__main__":
    main()
