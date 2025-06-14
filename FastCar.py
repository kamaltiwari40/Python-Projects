for number in range(101):
    if number % 3 == 0 and number % 7 == 0:
        print("FastCar")
    elif number % 3 == 0:
        print("Fast")
    elif number % 7 == 0:
        print("Car")
    else:
        print(number)