Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num = int(input("Enter number: "))

fact = 1

if num < 0:

    print("Negative Numbers invalid")

elif num == 0:

    print("The factorial of 0 is 1")

else:

    for i in range (1, num + 1):

        fact = fact * i

    print("The factorial of", num, "is", fact)