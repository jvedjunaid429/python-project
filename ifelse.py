age= 19
if age >17:
    print("you are old enough")
else:
    print("you are not old enough")

age = 20
country = "UK"
if age > 17 and country == "UK":
    print("yes i can serve you.")
else:
    print("you aren't old enough.")



import datetime
todays_date = datetime.date.today()
my_birthday = datetime.date(2020, 2, 19)
days_to_birthday = my_birthday - todays_date
print(days_to_birthday)


