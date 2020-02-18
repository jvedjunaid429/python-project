#def is similar to a variable but instead is  action
#def press_grind_beans():
#  print("Grinding for 20 seconds")

#press_grind_beans()

# def drink_order (size, type_of_drink):
#     print (" can i have {} from coffee machine please {}".format(size, type_of_drink))
    
# drink_order ("small", "coffee")

# drink_order ("medium", "latte")

# drink_order ("large", "hot chocolate")
# #return makes it easier so you dont have to rewrite the whole code everytime
# def add_up (num1,num2):
#     return num1 + num2

# print (add_up (4,5))
# print (add_up (3,1))

# def multiply_by_nine_fifths(celsius):
#  return celsius * (9/5)
# def get_fahrenheit(celsius):
#  return multiply_by_nine_fifths(celsius) + 32
 #print("The temperature is {}°F".format(get_fahrenheit(15)))

#def take_order(topping1,crust1,sauce5):
 #   print("can i get a 12inch Pizza with {},{}and {} in a tub".format(topping1,crust1,sauce5))
#take_order("donner", "cheesy crust" , "mayo")

#actual_pin = 7861
#balance = 500
#def cash_machine(pin, amount):
#    if pin == actual_pin and amount <= balance:
#        new_bal = balance - amount
#        print("Take your cash of £{}. Your new balance is £{}.".format(amount, new_bal))
#    elif pin == actual_pin and amount > balance:
#        print("insufficient funds")
#    else:
#        print("wrong pin enter correct pin")
#cash_machine(7861, 499)

#def multiply (num1,num2):
#    return num1 * num2

#print(multiply(2,3))

def sub_sandwich_order (top1,top2,top3,top4,top5):
    print("can i get a sub with {},{},{},with some {}".format(top1,top2,top3,top4,top5))
sub_sandwich_order("chicken","cheese","jalapenos","sweetcorn","salad")
