items = []

# Add an item to the shopping list
def add_item(item):
    items.append(item)

# Display all shopping items
def show_items():
    print("\nShopping Items:")
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

# Calculate the total price
def total_price(prices):
    return sum(prices)


# output:
# enter the item1:Bag
# enter price of Bag:500
# enter the item2:Kurtha
# enter price of Kurtha:3000
# enter the item3:Shoes
# enter price of Shoes:800
# enter the item4:Pant
# enter price of Pant:700
# enter the item5:T-Shirt
# enter price of T-Shirt:900

# Shopping Items:
# 1. Bag
# 2. Kurtha
# 3. Shoes
# 4. Pant
# 5. T-Shirt

# Total Bill:
# 5900.0