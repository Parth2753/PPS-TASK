def check_hydration(water):
    recommended = 2

    if water < 0 or water > 5:
        print("Invalid input: Water must be between 0 and 5 liters")
        return

    print("Hydration Status:")

    if water < recommended:
        print("Underhydrated")
        print("Drink more water to stay healthy")

    elif water == recommended:

        print("Adequately Hydrated")
        print("Good job! You are meeting your daily water requirement")
    else:

        print("Over-hydrated")
        print("You are above the recommended limit, be careful")
def main():
    try:
        water = float(input("Enter water consumed today (in liters): "))
        check_hydration(water)
    except ValueError:
        print("Invalid input! Please enter a numeric value")
main()



