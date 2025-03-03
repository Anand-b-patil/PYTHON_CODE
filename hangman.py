import random
words=["apple","samsung","vivo","redmi","motorola"]
chosen_word=random.choice(words).lower()
print("The chosen word is ",chosen_word)
display=[]
for char in chosen_word:
    display+="_"
print(display)
end_of_game=False
lives=6

while not end_of_game:
    letter=input("Choose the letter\n")
    if letter not in chosen_word:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            print("You lose")
            end_of_game = True
    for i in range(len(chosen_word)):
        if chosen_word[i]==letter:
            display[i]=letter
            
    print(display)
    
    if "_" not in display:
        end_of_game=True
        print("you Won")