def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() ==  answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing =False
        else:
            if attempt < 3:
                print("Attempts used:",attempt)
                guess = input("Sorry, Wrong answer. Guess again:")
            attempt = attempt + 1

    if attempt == 3:
        print("Your guesses are over.\n The Correct answer is:",answer)

score = 0
print("*****Guess the Answer*****")
print("*****You will have 2 attempts for each question*****")
guess_1 = input("In the 2015 World Cup final, who triggered New Zealand's collapse which saw them lose their last seven wickets for just 33 runs?\n")
check_guess(guess_1,"James Faulkner")
guess_2 = input("Who is MS Dhoni's only ODI wicket?\n")
check_guess(guess_2,"Travis Dowlin")
guess_3 = input("Who was the only player to be dismissed for 199 during the first edition of the WTC?\n")
check_guess(guess_3,"Faf Du Plessis")
print("******END OF QUIZ********")
print("Your score is:",score)