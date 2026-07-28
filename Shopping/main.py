import shopping

prices = []

# Input 5 shopping items
for i in range(5):
    item = input(f"enter the item{i+1}:")
    price = float(input(f"enter price of {item}:"))

    shopping.add_item(item)
    prices.append(price)

# Display all items
shopping.show_items()

# Display the total bill
print("\nTotal Bill:")
print(shopping.total_price(prices))