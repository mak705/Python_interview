##Quantity can be replaced by num_books, Saved in /tmp qbook.py
def book_cost(quantity):
   price = 25
   total_price = price * quantity
   return total_price

def shipping_cost(quantity):
    shipping_all = 3
    shipping_rest = 1
    total_shipping = shipping_all + (num_books - 1) * shipping_rest
    return total_shipping

num_books = int(raw_input('How many books do you want? '))
total_cost = book_cost(num_books)  + shipping_cost(num_books)
print "Shipping", num_books, "books costs", total_cost
print "shipping 1st book is 3Rs and rest book is 1Rs"
