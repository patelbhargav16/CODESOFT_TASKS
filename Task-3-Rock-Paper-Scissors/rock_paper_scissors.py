import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"

    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "scissors" and computer_choice == "paper")
        or (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"

    return "computer"


def main():
    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    print("=" * 45)
    print("       ROCK-PAPER-SCISSORS GAME")
    print("=" * 45)

    while True:
        print("\nChoose your option:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("\nEnter your choice (1-3): ")

        if choice not in ["1", "2", "3"]:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue

        user_choice = choices[int(choice) - 1]
        computer_choice = random.choice(choices)

        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("Result: It's a tie!")

        elif result == "user":
            print("Result: You win! 🎉")
            user_score += 1

        else:
            print("Result: Computer wins!")
            computer_score += 1

        print("\nScore:")
        print(f"You: {user_score} | Computer: {computer_score}")

        again = input(
            "\nDo you want to play another round? (y/n): "
        ).lower()

        if again != "y":
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()