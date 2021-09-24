Height = float(input("Enter your height in centimetres: \n"))
Weight = float(input("Enter your weight in kg: \n"))
Height = Height/100
BMI = Weight/(Height*Height)
print("Your BMI is:",round(BMI,3))

if(BMI>0):
    if(BMI<=16):
        print("You are Severly underweight!! \n Eat more calories and Start Lifting weights...")
    elif(BMI<=18.5):
        print("You are underweight! \n Eat more calories")
    elif(BMI<=25):
        print("You are healthy!!...Follow your current routine.")
    elif(BMI<=30):
        print("You are overweight...Grab your shoes.")
    else:
        print("You are Severly overweight!!... Pack your video games and Join a gym")
else:
    print("Please enter valid details")
    
