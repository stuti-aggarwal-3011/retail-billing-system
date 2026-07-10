# Store inventory data using parallel lists
item_names = ['Apple','Milk','Bread','Eggs']
item_prices = [40,25,80,7]
item_quantity = [25,50,75,100]
total_bill = 0.0

# Display initial stock to the user
print("Here are the items in the stock with their prices and quantity")

# Main shopping loop
while True:
    # Print the current stock status every round
    print(list(zip(item_names,item_prices,item_quantity)))
    
    # Get the item from the user and format it
    item = input("Enter the item you want to buy or type 'checkout' to finish: ").capitalize()
    
    # Check if the item exists in the stock lists
    if item in item_names:
        itempos = item_names.index(item)
        price = item_prices[itempos]
        qty = int(input("Enter the quantity you want to purchase: "))
        
        # Check if the requested quantity is available
        if qty > item_quantity[itempos]:
            print("Sorry, we have only",item_quantity[itempos], "units of" ,item)
        else:
            # Calculate price, update total bill, and reduce stock amount
            bill = qty*price
            total_bill += bill
            item_quantity[itempos] -= qty
            
    # Exit the loop if the user inputs checkout
    elif item == 'Checkout':     
        break
    else:
        print("Item not found, please pick from the menu.")
        
# Ask the user for a promotional discount code
code = input("Thank you! Do you have a promo code?(yes/no): ")

# Apply a 20% discount if the promo code is correct
if code == 'yes':
    print("Your bill is: ",total_bill)
    total_bill -= total_bill/5
    print("You got 20% discount! Your total bill is",total_bill)
    
# Apply a 10% loyalty discount if the bill is over 1000
elif total_bill > 1000:
    print("Your bill is: ",total_bill)
    total_bill -= total_bill/10
    print("You got 10% discount! Your total bill is",total_bill)
    
# Display the normal total bill if no discounts match
else:
    print("Your total bill is",total_bill)
