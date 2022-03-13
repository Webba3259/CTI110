nos = float(input("number of students you are ordering for? "))#nos = number of students
psp = float(input("how many students will be sharing each pizza? (1.5, 2, or 3)"))#psp = people sharing pizza
pn = round(nos/psp + .5) #pizzas needed before rounding, adding .5 to garuntee it always rounds up
pbt = (pn * 5) #price before tax
tax = (pbt * 0.06) #sales tax assuming 6%
pat = (pbt + tax) #price after tax
if (psp == 1.5 or psp == 2 or psp == 3):
    print("----Pizza Order--------")
    print("Number of Students :",nos)
    print("Pizzas Needed :",pn)
    print("price $",pat)
    print("--------------------------")


else:
    print("INVALID ENTRY!!!!")
    print("should have entered 1.5, 2, or 3")
    print("")#blank line
    print("Run Program Again")

