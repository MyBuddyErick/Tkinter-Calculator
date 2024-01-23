'''
import myscript as gui

print("1 plus")
print("2 minus")
print("3 times")
print("4 div")

choice = input("Choose Operation : ")
num1 = float(input("Enter Number 1 : "))
num2 = float(input("Enter Number 2 : "))

if choice == "1":
    print(num1, "+", num2, "=", (num1 + num2))
elif choice == "2":
    print(num1, "-", num2, "=", (num1 - num2))
elif choice == "3":
    print(num1, "*", num2, "=", (num1 * num2))
elif choice == "4":
    if num2 == 0.0:
        print("Hello World!")
    else:
        print(num1, "/", num2, "=", (num1 / num2))
else:
    print("I'm not doing that")

'''



#old stuff
'''
choice = gui.get_operation_choice()
num1 = gui.get_number1()
num2 = gui.get_number2()

choice = input("Choose Operation : ")
num1 = float(input("Enter Number 1 : "))
num2 = float(input("Enter Number 2 : "))

print("Choice:", choice)
print("Number 1:", num1)
print("Number 2:", num2)

'''