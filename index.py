def boxes_to_meters():
    response = input("list of numbers to plug in as x value of fx = 2.9x/100:  " )
    nums = response.split()
    for num in nums:
        x = float(num)
        y = (2.9 * x) / 100
        y_val = str(y)
        print(f"Input: {num} Output: {y_val}")



while True:
    choices = """
    1: Boxes To Meters
    2: End
    """
    print(choices)
    try:
        usr_choice = int(input("Enter the number coresponding to the action you want:  "))
    except:
        print("error")
        continue
    if usr_choice == 1:
        boxes_to_meters()
    elif usr_choice == 2:
        print("ending")
        break
    else:
        print("invalid input")
        continue