contactList= {
    1:{"Name":"Mom", "Phone":"306-3711","Age":"45"},
    2:{"Name":"Dad", "Phone":"306-4713","Age":"45"},
    3:{"Name":"Caed", "Phone":"721-4779","Age":"16"},
}
#print(contactList)

name=contactList[1]["Name"]
print(name)

for item in contactList.values():
    n=item["Name"]
    p=item["Phone"]
    a=item["Age"]
    print(f"A user in my contact list is {n} and thier phone number {p} and age is {a}")