
name = input(f"Enter your name: ")

buy_something = input(f"Hi {name}, Your initial balance is GH100. \n \
Would you like to purchase anything. Enter (Y) for yes  or (N) for no: ").upper()

if buy_something == "Y":
    name_of_item = input(f"\nEnter name of item to purchase: ")
    price_of_item = int(input(f"Enter price of item: "))

    current_balance = 100 - price_of_item
    print(f"Your current balance is GH{current_balance}.")

else:
    print("Thank You")

                    

