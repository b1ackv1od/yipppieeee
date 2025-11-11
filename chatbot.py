#this is self explanitory just a simple price listing

kawaii_items = {
    "Plushie": 8.99,
    "Enamal pins": 12.50,
    "Keychains": 7.25,
    "Kawaii Stationary": 1.99
}

##this part asks the name and age
def namer()
{
    print("HAIII im your chatbot assistant! im happy to help you what every your heart desires!")
    name = input("What is your name? ")
    print("Oh welcome! " + name + "! you have such a cute name!")
    age = input("how old are you? ")

if age <= 13
    print("Welcome!you will fit right in with our cute collection!")
    print("but you will need permistion to buy our things with a perent/gardian <3")

elif age >= 18
    print("Welcome! you will fit right in with our very cute collection<3")

}

# the main part of the chatbot that comunicates with the user, though theres a bug in it that its annoying and i cant seem to find it:/
def cute_chat():
    print("Welcome the Kawaii collection store!")
    while True:
        user_input = input("You: ").lower()
        if "kawii" in user_input:
            for item, price in kawaii_items.items():
                print(f"{item.title()}: ${price}")
        elif "order" in user_input:
            item = input("What would you like to buy? ").lower()
            if item in kawaii_items:
                print(f"You have ordered {item}. Your total is ${kawaii_items[item]:.2f}")
            else:
                print(" Sorry, we don't have that item available/out of stock.")
        elif "special" in user_input:
            print("We have a adorable deal! get two new stocks of cuteness!! >w<")
        
        elif "exit" in user_input or "bye" in user_input:
            print(" Thank you! See you soon!")
            break
        else:
            print("Sorry, I didn't understand that. Can you retype that again please? >-<'")
