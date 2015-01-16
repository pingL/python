# Negotiating with Bob
# A game in which you try to get the best possible deal out of Bob
# He is very predictable and has margins in the offering price which determine his actions
# This game also has score calculator
# By Atharv Sonwane

def main():
    price = 100000
    try_again = True
    print("Welcome to Negotiating with Bob! \n")
    print("You’re in high stake negotiation with Bob. The pressure is on to get the product you need for the best price "
         + " possible.")
    while try_again:
        print("\nThe starting price from Bob is £" + str(price))
        usr = int(input("Enter your offer: "))
        if usr <= 0.5 * price:
            print("Bob: I cant except that, who do you think I am ?")
            print("Bob has left the room! You have failed")
            success=False
            break
        if usr <= 0.75 * price:
            print("Thats not enough but I'l give you another try")
            continue
        if usr <= 0.9 * price:
            price *= 0.95
            print("OK, I will make my offer £" + str(price))
            continue
        if 0.9 * price < usr <= 100000:
            print("Great doing buisiness with you, it all yours")
            success=True
            break
        if usr > 100000:
            print("I will accept it but you\'re mad, by the way!")
            success=True
        break

    score = (1/usr) * 1000000000 
    if success:
        print("Well done, you have got the product, your score is: " + str(score))
    else:
        print("You could not do it.")
        print("GAME OVER")

    print("\nThank-you for playing Negotiation with Bob")
    print("Credits go to Atharv Sonwane and all those who taught him")
main()
