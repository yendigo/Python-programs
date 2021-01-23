x = int(input("Input the 1st number: "))
y = int(input("Input the 2nd number:"))
z = int(input("Input the 3rd number: "))
if x > y and y > z:
	print("The lowest:", z)
elif z > x and x > y:
	print("The lowest:", y)
elif y > z and z > x:
	print("The lowest:", x)
elif z > y and y > x:
	print("The lowest:", x)
elif x > z and z > y:
	print("The lowest:", y)
elif y > x and x > z:
	print("The lowest:", z)
else:
	print("All numbers are the same")
