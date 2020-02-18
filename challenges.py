#challenge 1
password = "codingdev"

if len(password) <8:
    print ("password too short")
else:
    print("password accepted")

    
#challenge 2
num = 21

if num % 3 == 0 or 5 == 0:
    print ("this number is divisible by 3 or 5")
else:
    print("this number is not divisible by 3 or 5") 

    
#challenge3
num= 12
if num % 3 == 0 or 5 == 0:
    print("fizzbuzz")
elif num % 3 == 0:
    print ("fizz")
elif num % 5 == 0:
    print ("buzz")
else:
    print("num")

#challenge4
num_int = 90909
num = str(num_int)
if num == num[::-1]:
    print("This is a palindrome.")
else:
    print("This is not a palindrome")

#challenge5
time = 8
place_of_work = "manchester"
town_of_home = "oldham"

if time == 7:
    print("im at home in {}".format(town_of_home))
elif time == 8:
    print("i am commuting between {} and {}".format(town_of_home, place_of_work))
elif time == 9:
    print("I'm at {}".format(place_of_work))
else:
    print("I am in limbo.")

#challenge6
num1 = 2
num2 = 5
num_sum = num1 + num2
if num_sum % 2 == 0:
    print("this is even")
else:
    print("This is odd.")

#final challenge 1
age = 55

if age < 18:
    print (" child ticket is £8.00 ")
elif age < 60:
    print ("adult ticket is £10.95")
else:
    print ("senior ticket is £7.50")