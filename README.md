# 🧮 Expense Tracker with Bubble Sort

A small Python expense tracker built to practise a classic sorting algorithm. Add what you bought, see the total, and sort your expenses from cheapest to most expensive using **Bubble Sort**, written by hand instead of Python's built-in `sort()`.

It comes in two versions:

| File | Version |
|---|---|
| `expencetracker.py` | Command-line menu |
| `Gui.py` | Desktop window built with Tkinter |

## Features

- Add an expense (name and amount)
- View all expenses
- Sort them by amount with Bubble Sort
- See the total, with a friendly warning if you spent more than 1,000

## How Bubble Sort works here

The list is scanned again and again. Each pass compares neighbouring expenses and swaps them if they're in the wrong order, so the largest amount "bubbles" to the end:

```python
for i in range(len(expenses)):
    for j in range(0, len(expenses) - i - 1):
        if expenses[j][1] > expenses[j + 1][1]:
            expenses[j], expenses[j + 1] = expenses[j + 1], expenses[j]
```

- **Time complexity:** O(n²) comparisons in the worst case
- **Space complexity:** O(1), since it sorts in place

That's fine for a handful of expenses. Python's built-in `sorted()` (Timsort, O(n log n)) would be the right choice for large lists.

## Run it

Needs Python 3. Tkinter is included with most Python installs.

```bash
python expencetracker.py   # command-line version
python Gui.py              # window version
```

## Limitations

Expenses are kept in memory only, so they're lost when the program closes. Saving to a file would be the natural next step.
