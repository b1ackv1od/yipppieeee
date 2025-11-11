kawaii_items = {
    "Plushie": 8.99,
    "Enamal pins": 12.50,
    "Keychains": 7.25,
    "Kawaii Stationary": 1.99
}

def cute_chat():
    print("Welcome the Kawaii collection store!")
    while True:
        user_input = input("You: ").lower()
        if "kawii" in user_input:
            for item, price in kawaii_items.items():
                print(f"{item.title()}: ${price}")
        elif "order" in user_input:
            item = input("What would you like to order? ").lower()
            if item in kawaii_items:
                print(f"Bot: You have ordered {item}. Your total is ${kawaii_items[item]:.2f}")
            else:
                print(" Sorry, we don't have that item available/out of stock.")
        elif "special" in user_input:
            print("We have a adorable deal! get two new stocks of cuteness!! >w<")
        elif "reservation" in user_input:
            name = input("Name for reservation: ")
            time = input("Time for reservation: ")
            print(f"Bot: Reservation made for {name} at {time}.")
        elif "exit" in user_input or "bye" in user_input:
            print("Bot: Thank you! See you soon!")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Can you rephrase?")
