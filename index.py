response = input("list of numbers to plug in as d value of fx = 2.9x/100:" ))
nums = response.split()
for num of nums:
	x = float(num)
    y = (2.9 * x) / 100
    y_val = str(y)
    print(f"Input: {num} Output: {y_val}")