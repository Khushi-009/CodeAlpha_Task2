# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700
}

# Dictionary to store user's portfolio
portfolio = {}

print("Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Input loop
while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    else:
        print("Stock not available.")

# Calculate total investment
total = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    print(f"{stock}: {qty} x ${price} = ${investment}")
    total += investment

print(f"\nTotal Investment: ${total}")

# Optional: Save to file
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} x ${price} = ${investment}\n")
        file.write(f"\nTotal Investment: ${total}")
    print("Portfolio saved to portfolio.txt")
