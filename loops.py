for i in range(10):
 print(i)

import random
for i in range(6):
    print(random.randint(1,50))
#this creats a loop and will give random data

for i in range (9,0):
    print(i)

for i in range (9,-1,-1):
    print(i)

fav_films = ["iron man", "the dark knight", "ghostbusters","deadpool 2"]
fav_films.append("suicide squad",)
fav_films.append("bad boys 2")
print (fav_films)

for i in fav_films:
    print(i)

def film_check(fav_films):
    if fav_films [2] == "ghostbusters":
        print("yay!")
    else:
        print("booo!")
film_check(fav_films)

        
