tock_prices = {
    "sugar": 180,
    "cooking_oil": 250,
    "coffee": 140,
    "spices": 130,
    "salt": 310
}

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", list(stock_prices.keys()))
print()

portfolio = {}   
total_value = 0  

n = int(input("How many stocks do you want to add? "))

for i in range(n):
    stock_name = input("Enter stock name (e.g. salt): ").lower()

    if stock_name not in stock_prices:
        print("Sorry, that stock is not in our list. Try again.\n")
        continue 

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    value = price * quantity

    portfolio[stock_name] = {"quantity": quantity, "price": price, "value": value}

    total_value += value 
    print(f"Added {quantity} shares of {stock_name} at ${price} each = ${value}\n")

print("\n=== Your Portfolio Summary ===")
for stock, info in portfolio.items():
    print(f"{stock}: {info['quantity']} shares x ${info['price']} = ${info['value']}")

print(f"\n Total Investment Value: ${total_value}")

with open("portfolio_result.txt", "w") as file:
    file.write("=== Portfolio Summary ===\n")
    for stock, info in portfolio.items():
        file.write(f"{stock}: {info['quantity']} shares x ${info['price']} = ${info['value']}\n")
    file.write(f"\nTotal Investment: ${total_value}\n")

print("\n Portfolio saved to portfolio_result.txt")