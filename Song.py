contactList= {
    1:{"Name":"Mom", "Phone":"306-3711","Age":"45"},
    2:{"Name":"Dad", "Phone":"306-4713","Age":"45"},
    3:{"Name":"Caed", "Phone":"721-4779","Age":"16"},
}
#print(contactList)

#name=contactList[1]["Name"]
#cprint(name)

person=input("What person do you want? ")
print("Caed,Mom,Dad")

if person == "Mom":
    mom=contactList[1]["Name"],contactList[1]["Phone"],contactList[1]["Age"]
    print(mom)
elif person == "Dad":
    dad=contactList[2]["Name"],contactList[2]["Phone"],contactList[2]["Age"]
    print(dad)
elif person == "Caed":
    Caed=contactList[3]["Name"],contactList[3]["Phone"],contactList[3]["Age"]
    print(Caed)
else:
    print("That isnt a valid name")
    person=input("What person do you want? ")