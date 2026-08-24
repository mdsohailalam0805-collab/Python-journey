import random
import matplotlib.pyplot as plt

number = random.randint(1, 100)
attempts = 0
attempt_history = []

print("🎯 Number Guessing Game")
print("Guess a number between 1 and 100")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    attempt_history.append(guess)

    if guess < number:
        print("🔵 Too Low!")

    elif guess > number:
        print("🔴 Too High!")

    else:
        print(f"🟢 Correct! You guessed it in {attempts} attempts.")
        break

plt.figure(figsize=(9, 5))

plt.plot(
    range(1, attempts + 1),
    attempt_history,
    marker="o",
    color="purple",
    linewidth=2,
    markerfacecolor="orange",
    markeredgecolor="black"
)

plt.axhline(
    number,
    color="green",
    linestyle="--",
    linewidth=2,
    label=f"Correct Number: {number}"
)

plt.fill_between(
    range(1, attempts + 1),
    attempt_history,
    number,
    alpha=0.15,
    color="purple"
)

plt.title("🎯 Number Guessing Game Progress", fontsize=16)
plt.xlabel("Attempt Number")
plt.ylabel("Guessed Number")

plt.grid(
    True,
    linestyle="--",
    alpha=0.4
)

plt.legend()
plt.tight_layout()
plt.show()