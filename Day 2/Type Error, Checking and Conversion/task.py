from operator import truth

name_of_the_user = input("Enter your name")
lenth_of_name =  len(name_of_the_user)

print(type(name_of_the_user)) #str
print(type(lenth_of_name)) #int

print("Numbers in the name are " + str(lenth_of_name))
