# CTI-110
# P2HW2 - Score Avg
# Your Name 
# Date
#


S1 = eval (input("Enter score#1 :"))
S2 = eval (input("Enter score#2 :"))
S3 = eval (input("Enter score#3 :"))
S4 = eval (input("Enter score#4 :"))
S5 = eval (input("Enter score#5 :"))
S6 = eval (input("Enter score#6 :"))
S7 = eval (input("Enter score#7 :"))
#creating empty lines, i don't know how else to do this
print()
print()
#empty lines created
#i don't know if the ammount of - matters, its hard to count in the picture
print("-----------Results-----------")
#class average
Classaverage = [(S1), (S2), (S3), (S4), (S5), (S6), (S7)]
Classaverage.sort()
#i can't for the life of me figure out how to round [:1], it keeps giving errors
print("lowest Score:", Classaverage[:1])
#removes the lowest score
Classaverage.remove(min(Classaverage))
print("Modified List:", Classaverage)
average = sum(Classaverage) / len(Classaverage)
print("Scores Average:", round(average, 2))
print("----------------------------------")
