# program to request prices and calculate total ammount
    # Date 2/24/2022
    # CTI-110 P2HW1 - Total Purchases
    # Webb Austin
    #
item1 = eval (input("enter the price of item #1") )
item2 = eval (input("enter the price of item #2") )
item3 = eval (input("enter the price of item #3") )
item4 = eval (input("enter the price of item #4") )
item5 = eval (input("enter the price of item #5") )
#item inputs
subtotal = (item1 + item2 + item3 + item4 + item5)
salestax = (subtotal * 0.07)
total = (subtotal + salestax)
#math
print()
print("------Results------")
print("Subtotal",round( item1 + item2 + item3 + item4 + item5, 2))
print("Sales Tax:",round( subtotal * 0.07, 2) )
print("Total:",round( total, 2) )
