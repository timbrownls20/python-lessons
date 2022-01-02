person = input("Say hello to: ")
person = person.strip()
person = person.capitalize()

if person == "Sophie":
    print (person + " is epic!")
elif person == "Mum" or person == "Mummy":
    print ("Love you " + person)
elif person == "Rosie" or person == "dogdog":
    print ("WoofWoof " + person)
elif person == "Dad" or person == "Daddy":
    print ("you taught me this " + person)
else:
    print ( person + " is pretty cool") 
