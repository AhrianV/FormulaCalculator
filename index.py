import math

def boxes_to_meters():
    response = input("list of numbers to plug in as x value of fx = 2.9x/100:  " )
    nums = response.split()
    for num in nums:
        try:
            x = float(num)
        except:
            return"error"
        y = (2.9 * x) / 100
        y_val = str(y)
        print(f"Input: {num} Output: {y_val}")
        
def circular_velocity():
    constant = input("Is radius constant? (y or n):  ")
    if constant == "n":
        response = input("list of numbers to plug in as r value of V = 2(pie)r/T:  " )
        num_list1 = response.split()
        return "comming soon"
    else:
        num = input("number to plug in as r value of V = 2(pie)r/T:  " )
        response2 = input("list of numbers to plug in as T value of V = 2(pie)r/T:  " )
        num_list2 = response2.split()


        for p in num_list2:
            try:
                radius = float(num)
                period = float(p)
            except:
                return"error"
            y = (2 * math.pi * radius) / period
            y_val = str(y)
            print(f"R Input: {num} T Input: {period} Output/Velocity: {y_val}")






while True:
    choices = """
    0: End
    1: Boxes To Meters
    2: Periord and Radius to Circular Velocity
    """
    print(choices)
    try:
        usr_choice = int(input("Enter the number coresponding to the action you want:  "))
    except:
        print("error")
        continue
    if usr_choice == 1:
        boxes_to_meters()     
    elif usr_choice == 0:
        print("ending")
        break
    elif usr_choice == 2:
        circular_velocity()
    else:
        print("invalid input")
        continue