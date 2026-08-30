"""A beginner-friendly command-line expense tracker."""


def main():
    """Collect expense amounts and display their total."""
    total = 0.0

    print("=== Expense Tracker ===")
    print("Enter an expense amount, or type 'done' to finish.")

    while True:
        user_input = input("Expense amount: ").strip()

        if user_input.lower() == "done":
            break

        try:
            new_expense = float(user_input)

            if new_expense < 0:
                print("Please enter a positive amount.")
                continue

            # Accumulator logic: add each new expense to the running total.
            total = total + new_expense
            print(f"Added: {new_expense:.2f}")
        except ValueError:
            print("Invalid input. Enter a number such as 100, 50, or 20.")

    print(f"\nTotal Spent: {total:.2f}")


if __name__ == "__main__":
    main()
