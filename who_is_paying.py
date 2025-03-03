import random
names=input("Give everybodys name separated by comma\n")
name1=names.split(",")
x=len(name1)
name=random.randint(0,x-1)
print(name1[name],"is going to by the meal today")