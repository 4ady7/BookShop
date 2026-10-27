# BookShop

A customer orders a book, the shop ships that order, and an invoice that includes the shipping cost is stored so it can be searched later.

## Requirements

- Python 3
- Tkinter, for the window

The `python3` from Homebrew on this machine does not include Tkinter. Use Anaconda’s Python to open the window:

```bash
/opt/anaconda3/bin/python3 bookstore_gui.py
```

If your `python3` already has Tkinter, `python3 bookstore_gui.py` is enough. The console programs do not need Tkinter.

## Run the window

1. **Add Customer** — name, an 11-digit phone number starting with `07`, and an email with one `@` and one dot.
2. **Add Book to Stock** — title, author, and a price greater than 0 with at most two decimal places, such as `5.78` or `10.00`.
3. Choose the customer and the book, then **Place the Order**.
4. **Shipping Options**. Tick **Is it an Urgent Order?** for urgent delivery, then **Calculate Shipping**.
5. **Invoice Generation**. The invoice uses the order you placed and the shipping cost just calculated.
6. **View All Invoices**, or **SearchID** with the full number, such as `INV0001`.

Standard shipping is £3.95. Urgent shipping is £5.45. The invoice total is the book price plus that shipping cost. Invoice numbers start at `INV0001`.

Placing another order before generating an invoice replaces the open order. Shipping then has to be calculated again. An urgent shipment is counted once.

## Example

Adam Fisher buys *Prince Caspian* by C.S. Lewis.

| Item | Amount |
| --- | --- |
| Book | £5.78 |
| Urgent shipping | £5.45 |
| Invoice `INV0001` | £11.23 |

Search `INV0001` to find that invoice. Search `INV0004` and the repository reports that nothing was found.

Run the same example without clicking through the window:

```bash
/opt/anaconda3/bin/python3 example.py
```

## Console

`bookstore_core.py` is the first design. `bookstore_core_inher.py` is the same shop after the inheritance refactor, and it is the module the window uses.

```bash
python3 bookstore_core.py
python3 bookstore_core_inher.py
```

Each program asks for one customer, then adds two more customers and three books, ships the orders, prints the invoice totals, and searches for `INV0004`. A valid first customer is:

```text
Adam Fisher
07123456789
adamFisher@gmail.com
```

## Classes

`bookstore_core_inher.py` is the design the window imports.

| Class | Role |
| --- | --- |
| `Person` | Name, phone, and email |
| `Customer(Person)` | A person who orders books |
| `Product` | Book title and price |
| `Stock(Product)` | A product plus the author |
| `Order` | One customer and one stock item |
| `Shipping` | The order, ship date, and shipping cost |
| `Invoice` | Invoice number, book, shipping, and total |
| `BookStore` | The message and the invoice repository, including `search_invoice` |

`bookstore_core.py` has the same shop without `Person` and `Product`. `bookstore_gui.py` is the Tkinter window.

## Files left out of git

`.gitignore` ignores `*.docx` and `*.pdf`.
