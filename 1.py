sum=0
score=[56,89,69,88,45,75,55,99,80,90,79]

for i in score: 
    sum=sum+i
avg=sum/len(score)

print("Average= ",avg)
high=score[0]
for i in range(0,len(score)):
    if high <= score[i]:
        high=score[i]
        
print("Highest score is ",high)

for i in range(0,len(score)):
    if score[i]%2==0:
        sum+=score[i]

print("The even sum is ", sum)

