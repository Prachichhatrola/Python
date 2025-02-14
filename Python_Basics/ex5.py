age = int(input("What is your age?: "))

def checkDriverAge(driverage=0):
    if driverage < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif driverage > 18:
        print("Powering On. Enjoy the ride!");
    elif driverage == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge(age)
