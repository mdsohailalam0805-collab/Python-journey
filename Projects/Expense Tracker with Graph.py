
# Expense Tracker with Graph

import matplotlib.pyplot as plt

expenses = {}
total_expense = 0

print("💰 Daily Expense Tracker")

while True:
    category = input("\nEnter expense category (or 'done' to finish): ")

    if category.lower() == "done":
        break

    amount = float(input("Enter expense amount: "))

    expenses[category] = amount
    total_expense += amount

print("\n----- Expense Summary -----")

for category, amount in expenses.items():
    print(f"{category}: ₹{amount}")

print(f"\nTotal Expense: ₹{total_expense}")

categories = list(expenses.keys())
amounts = list(expenses.values())

colors = ["red", "blue", "green", "orange", "purple", "cyan"]

plt.figure(figsize=(8, 5))

plt.bar(
    categories,
    amounts,
    color=colors[:len(categories)],
    edgecolor="black"
)

plt.title("💰 Daily Expense Tracker")
plt.xlabel("Expense Category")
plt.ylabel("Amount (₹)")

for i, amount in enumerate(amounts):
    plt.text(i, amount + 5, f"₹{amount}", ha="center")

plt.tight_layout()
plt.show()