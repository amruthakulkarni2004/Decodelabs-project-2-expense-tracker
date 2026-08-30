# Expense Tracker

A beginner-friendly Python command-line project that records expense amounts and calculates the total amount spent.

## Features

- Accepts expense amounts continuously (for example: `100`, `50`, and `20`).
- Adds each valid expense to a running total using an accumulator.
- Displays the final **Total Spent** when the user types `done`.
- Handles invalid entries without stopping the program.
- Uses only Python's built-in features; no external packages are needed.

## Requirements

- Python 3.x

## How to Run

1. Open a terminal in this project folder.
2. On Windows, run:

   ```bash
   py main.py
   ```

   On macOS or Linux, use `python3 main.py` (or `python main.py` if that is how Python is installed).

3. Enter expense amounts one at a time.
4. Type `done` when you have finished entering expenses.

## Sample Output

```text
=== Expense Tracker ===
Enter an expense amount, or type 'done' to finish.
Expense amount: 100
Added: 100.00
Expense amount: 50
Added: 50.00
Expense amount: 20
Added: 20.00
Expense amount: done

Total Spent: 170.00
```

## How It Works

The variable `total` starts at `0.0`. Every time the user enters a valid expense, the program uses this accumulator statement:

```python
total = total + new_expense
```

This adds the new expense to the previous total. A `while` loop keeps asking for expenses until the user types `done`.

## Files

- `main.py` — the Expense Tracker program.
- `README.md` — project overview and instructions.
