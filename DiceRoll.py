import random 

min_val = 1
max_val = 6

roll = input("Roll the Dice-Yes or No:\n").capitalize()

while roll == "Yes":

    print("Rolling the Dices....")
    print('The values are:')
    print(random.randint(min_val,max_val))
    print(random.randint(min_val,max_val))
    roll = input("Roll the Dices Again?").capitalize()
    if roll == "No":
        print("******END*******")
    else:
        print("Enter a valid input...")