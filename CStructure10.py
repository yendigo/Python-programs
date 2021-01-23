x = int(input("Input first number: "))
y = int(input("Input second number:"))
z = int(input("Input third number: "))
if x == y and y == z and x == z:
	print("All numbers are equal")
elif x != y and y != z and x != z:
	print("All numbers are different")
elif x == y and y != z and x != z:
	print(z, "is different")
elif x == z and z != y and x != y:
	print(y, "is different")
elif z == y and y != x and z != x:
	print(x, "is different")