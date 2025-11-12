# Create a number guessing game.
# Write a program that takes a number and prints whether it’s even/odd, and also prints its square using a loop.


import random

print("=== Number Guessing Game ===")

# 1. Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# 2. Ask the user to guess
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess < 1 or guess > 10:
            print("❌ Please guess a number within the range 1–10.")
            continue

        if guess == secret_number:
            print("🎉 Correct! You guessed the number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

# 3. Check if the number is even or odd
if secret_number % 2 == 0:
    print(f"\n✅ The secret number {secret_number} is even.")
else:
    print(f"\n✅ The secret number {secret_number} is odd.")

# 4. Print its square using a loop
print("\n📘 Displaying the square of the number using a loop:")
for i in range(1, 2):  # simple loop to demonstrate the concept
    print(f"The square of {secret_number} is {secret_number ** 2}")

print("\n=== Game Over ===")