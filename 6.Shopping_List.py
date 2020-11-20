shopping_dict = {}
print("Welcome from Wikiki's Store")
print("***********************")
user = input("Enter your name: ")
while user != 'Off':
    item = input("Enter your item: ")
    quantity = int(input("Enter the quantity: "))

    if user not in shopping_dict:
        shopping_dict[user] = {}
    if item in shopping_dict[user]:
        shopping_dict[user][item] += quantity
    else:
        shopping_dict[user][item] = quantity
    user = input("Enter your name: ")

print(shopping_dict)
print()

for user in shopping_dict:
    print(user)
    for item, quantity in shopping_dict[user].items():
        print('{} : {} '.format(item, quantity))

    print("****************************")
