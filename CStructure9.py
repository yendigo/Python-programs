x = int(input("Input first number: "))
y = int(input("Input second number:"))
z = int(input("Input third number: "))
if x < y and y < z:
	print("Increasing order")
elif z < y and y < x:
	print("Decreasing order")
else:
	print("Neither increasing or decreasing order")
