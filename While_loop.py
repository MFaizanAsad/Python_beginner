# This is a program to use a while loop
capital_cities =["Islamabad", "Delhi", "Dhaka","Helsinki","Moscow","Washinton"]
user_input = ""
while user_input != "q":
    user_input = input("Enter a city name, or q to quit:")
    if user_input != "q":
        for a_capital_city in capital_cities:
            if user_input == a_capital_city:
                print("\n it's one of the capital city")
                break
                

