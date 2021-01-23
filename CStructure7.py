x = int(input("Input the 1st number: "))
y = int(input("Input the 2nd number:"))
z = int(input("Input the 3rd number: "))
if x < y and y < z:
	print("The greatest:", z)
elif z < x and x < y:
	print("The greatest:", y)
elif y < z and z < x:
	print("The greatest:", x)
elif z < y and y < x:
	print("The greatest:", x)
elif x < z and z < y:
	print("The greatest:", y)
elif y < x and x < z:
	print("The greatest:", z)
else:
	print("All numbers are the same")
