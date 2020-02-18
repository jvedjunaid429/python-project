def search():
    print("Search room")
def hallway():
    print("Hallway")
def lounge():
    print("lounge. Enter 'hallway' or 'search'")
    response = input("What do you do? ")
    if response == "hallway":
        hallway()
    elif response == "search":
        search()
    else:
        print("Invalid response")
        lounge()
lounge()
def upstairs_hallway():
    print("upstairs hallway. Enter 'bedroom' or 'bathroom' or 'downstairs hallway'?")
    response = input("What do you do? ")
    if response == "bathroom":
        bathroom()
    elif response == "bedroom":
        bedroom()
    elif response == "downstairs hallway":
        stairs()
    else:
        print("Invalid response")
        ()
def bedroom():
    print("bedroom. Enter 'upstairs hallway' or 'search'")
    response = input("What do you do? ")
    if response == "search":
        search()
    elif response == "upstairs hallway":
        upstairs_hallway()
    else:
        print("Invalid response")
        ()
def bathroom():
    print("bathroom. Enter 'upstairs hallway' or 'search"")
    response = input("What do you do? ")
    if response == "search":
        search()
    elif response == "upstairs hallway":
        upstairs_hallway()
    else:
        print("Invalid response")
        ()
def bunker():
    print("bunker. Enter 'yes' or 'no'")
    response = input("What do you do? ")
    if response == "yes":
       bunker()
    elif response == "no":
        ()
    else:
        print("Invalid response")
        ()
def ():
    print(". Enter '' or ''")
    response = input("What do you do? ")
    if response == "":
        ()
    elif response == "":
        ()
    else:
        print("Invalid response")
        ()
def ():
    print(". Enter '' or ''")
    response = input("What do you do? ")
    if response == "":
        ()
    elif response == "":
        ()
    else:
        print("Invalid response")
        ()













