## Create an console interface for ordering from a menu, 
## it will let customers order and add as many menu items as they want
menu = {"grilled chicken": "$11.00", "tacos": "$15.00", "Vegetable pasta": "$10:00"}
orders = []
# Add the user what they want to order as: what would you like to order? (Q to quit)
# while the order is not equal for Q for quit, find the order and add it to the list if it exists
# else let the customer know that the `Menu item does not exist`    
# See if the customer wants to order anything else `Anything else? (Q to Quit)`
total = 0

""" while True:
    print("Welcome to our restaurant I hope you are having an excellent day!!! :)")
    print("Press 'S' to Show Menu")
    print("Press 'Q' to quit")
    answers = ["s", "S", "q", "Q"]
    answer = input("Ingrese una letra: ")
    

    if answer not in answers:
        print("You need to chose betweet S or Q the answer should only has a leght of 1 letter")
    else:
        if answer.lower() == "s":
            print("Our menu for today is: ") 
            for plate, price in menu.items():
                print(f"{plate} : {price}")

           
            order = input("Enter your order: ")

            if order in menu:
                orders.append(order)
                print("You can use n or no to finish with this menu a get your order")
                answer = input("Is there anything else that you would like to add?")
                if answer.lower() == "no" or answer.lower() == "n":
                    for ord in range(len(orders)):
                        print(ord)
                        print("Su order ha sido {}".format(orders[ord]))
                    break
            else:
                print("I'm sorry but we don't have that food, Try with a different one")
        else:
            print("Thank you so much for contacting us, Have a nice one!!!...")      
            break   """


import random

num = random.randint(1, 10)


for i in range(3):
    guess = int(input("Ingrese un numero: "))

    if guess == num:
        print(f"You win the number is {num}")
        break
else:
    print(f"You lost the number is {num}")    