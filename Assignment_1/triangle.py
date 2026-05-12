#6. Write a Program to input two angles from user and find third angle of the
#triangle.

angle1 = int(input("Enter the first angle: "))
angle2 = int(input("Enter the second angle: "))


angle3 = 180 - (angle1 + angle2)

print(f'third angle is:{angle3}')