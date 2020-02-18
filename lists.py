faviroute_songs = [
    "drake and future - life is good",
"eminem - godzilla",
"mhuncho - tranquillity"]
faviroute_songs[2] = "roddy rich - the box"
faviroute_songs.append("eminem - godzilla")
faviroute_songs.pop()
print(faviroute_songs)

fav_sites = [
    "facebook.com",
"reddit.com",
"youtube.com"
]
fav_sites.append("google.com",)
#.append adds another item onto the list.
fav_sites.append("yahoo.com")
#you have to do 1 item for each time you want to append it wont do multiple.
fav_sites.pop()
#.pop removes the last item you added on the list.
fav_sites.remove("google.com")
#.remove gets rid of the item you want but you jave to put it as a string in the brackets.
fav_sites.reverse()
#.reverse reverses the order of the list.
fav_sites.sort()
#.sort sorts the list how you want.
print(fav_sites.count("facebook.com"))
#.count can show yoiu the number of items on your list you have to use it with the brackets.
fav_sites.extend("facebook.com")
#.extend extends the item you want you just have to put in the brackets.
print(fav_sites)

people = ["junaid", "ali", "tom"]
people.insert(0, "mandy")
print(people)
#i can use (0,example) to add a item to the start of a list.

faviroute_cars = ["audi","bmw","mercedes"]
faviroute_cars.insert(0,"jaguar")
print(faviroute_cars)

