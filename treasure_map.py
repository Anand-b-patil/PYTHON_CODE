row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]

map=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}\n")

print("Where do you want to put a treasure enter row and column \n")
row=int(input("Row"))
column=int(input("Column"))

map[row-1][column-1]="x"
print(f"{row1}\n{row2}\n{row3}\n")

