print("Assignment 2.1")
print("First task")

''' THIS IS A PROGRAM THAT WILL TELL YOU WHICH CHARACTER YOU ARE FROM MONEY HEIST '''

print("THIS IS A PROGRAM THAT WILL TELL YOU WHICH CHARACTER YOU ARE FROM MONEY HEIST")
print()
print ("Please type specific [as it is case sensitive]")
print ()
d1 = input("In a hiest would you be: \nThe serial planner \nThe spontaneous type")

if d1 == "The serial planner":
    print()
    d2 = input("A caring soul \nA warrior spirit ")
    if d2 == "A warrior spirit":
        print()
        d3 = input ("Wise monk \nCunning fox")
        if d3 == "Wise monk":
            print()
            d4 = input ("A team player \nThe puppet master")
            if d4 == "A team player":
                print()
                print("You are NAIROBI")
            else:
                print()
                print("You are PALERMO")
        else:
            print()
            d5 = input ("Precision \nUnleashing chaos")
            if d5 == "Precision":
                print("You are \"THE PROFESSOR\"")
            else:
                print("You are BOGOTA")
    else:
        print()
        d6 = input ("Strictly professional \nOpen to romance")
        if d6 == "Strictly professional":
            print()
            d7 = input("All for 1 \n1 for all")
            if d7 == "All for 1":
                print("You are STOCKHOLM")
            else:
                print()
                print("You are OSLO")
        else:
            print()
            d8 = input("Misson over love \nLove over mission")
            if d8 == "Mission over love":
                print("You are DENVER")
            else:
                print()
                print("You are RIO")
else:
    print()
    d9 = input("Impulsive by nature \nCalm under pressure")
    if d9 == "Impulsive by nature":
        print()
        d10 = input("Mind \nMuscle")
        if d10 == "Mind":
            print()
            d11 = input("Good cop \nBad cop")
            if d11 == "Good cop":
                print()
                print("You are LISBON")
            else:
                print()
                print("You are ARTURO")
        else:
            print()
            d12 = input("Romance \nTough love")
            if d12 == "Romance":
                print()
                print("You are TOKYO")
            else:
                print()
                print("You are GANDIA")
    else:
        print()
        d13 = input("Mission first \nPeople first")
        if d13 == "Mission first":
            print()
            d14 = input("In the frontlines \nBehind the curtains")
            if d14 == "In the frontlines":
                print()
                print("You are BERLIN")
            else:
                print()
                print("You are MOSCOW")
        else:
            print()
            d15 = input("Precision \nUnleashing chaos")
            if d15 == "Precision":
                print()
                print("You are MARSEILLE")
            else:
                print()
                print("You are HELSINKI")
print()
print()
print("I hope you liked this program")
print("BYE")
print("😊")
print()

print()
print()
print()


print("Second task")

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
print()
print()
print()

print("Third task")
'''This is a calculator''' 


#takes in the operator
print("What operation do you want to do ?")
print('+ \n- \n* \n/ \n** \n// \n')
operator = input()
print()
print()

N2 = input('Enter your first number:')
num1 = int(N2)
print()
n3 = input('Enter your second number:')
num2 = int(n3)
print()
fd = num1 // num2

#conditions
if operator == '+':
    add = num1 + num2
    print(add)
elif operator == '-':
    sub = num1 - num2
    print(sub)
elif operator == '*':
    mul = num1 * num2
    print(mul)
elif operator == '/':
    div = num1 / num2
    print(div)
elif operator == '**':
    mod = num1 ** num2
    print(mod)
else:
   print(fd) 
