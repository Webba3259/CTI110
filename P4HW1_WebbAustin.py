# CTI-110
# P4HW1 - Score List
# Webb Austin
# Date 3/26/2022
#
S1 = int (input("How many scores do you want to enter? :"))
S3 = []
count = 1
while S1 > 0:
    print('Enter score number #',count,':')
    S2 = eval(input())
    if S2 <0 or S2 >100:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        print('Enter score #',count,'again:',)
        S2 = eval(input())
    else:
        S3.append(S2)
        count = count + 1
    S1 = S1 - 1
#creating empty lines, i don't know how else to do this
print()
print()
#empty lines created
#i don't know if the ammount of - matters, its hard to count in the picture
print("-----------Results-----------")
#class average
Classaverage =(S3)
Classaverage.sort()
#i can't for the life of me figure out how to round [:1], it keeps giving errors
print("lowest Score  :", Classaverage[:1])
#removes the lowest score
Classaverage.remove(min(Classaverage))
print("Modified List :", Classaverage)
average = sum(Classaverage) / len(Classaverage)
print("Scores Average:", round(average, 2))
if average >= 90:
    print('Grade         : A')
elif average >= 80:
    print('Grade         :B')
elif average >= 70:
    print('Grade         :C')
elif average >= 60:
    print('Grade         :D')
elif average <60:
    print('Grade         :F')
print("----------------------------------")
