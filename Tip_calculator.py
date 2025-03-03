
print("Welcome to tip calculator")
total_bill=float(input("What was the total bill?\n"))
tip=float(input("How much tip would you like to give 10, 12 or 15 ?\n"))
total_tip=(total_bill*tip)/100

person=float(input("How many people to split the bill?\n"))

print("Each person should pay ",round((total_bill+total_tip)/person))


