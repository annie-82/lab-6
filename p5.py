Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Syed Hussain
# 08/14/2022
#Write a program to compute the conversion given a user input value.
#Print this value as well as the calculated value using the degrees function in the math modul

radians = input("Give me a radian: ")
print("The given radian is",radians)
degrees = math.degrees(int(radians))
print("The degree of the given radian is :",degrees)