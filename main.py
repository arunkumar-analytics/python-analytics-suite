"""

"""
Python Multi-Tool Suite
Author: Your Name
Date: 2026
Description: Collection of 6 utility tools for data analysis tasks
"""

import sys

def get_valid_int(prompt):
    """Ensure user enters a valid integer"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")

def first_five(text):
    """Extract first 5 characters from a string"""
    return text[:5] if len(text) >= 5 else text

def profit_loss(cost_price, selling_price):
    """Calculate profit or loss amount"""
    Rs = '\u20B9'
    if selling_price > cost_price:
        profit = selling_price - cost_price
        return f"Profit :{Rs}{profit}"
    else:
        loss = cost_price - selling_price
        return f"Loss :{Rs}{loss}"

def perfect_squares(limit):
    """Generate perfect squares up to given limit"""
    squares = []
    for i in range(1, int(limit**0.5) + 1):
        squares.append(i*i)
    return squares

def multiples(limit, multiplier):
    """Find multiples within a given range"""
    return list(range(multiplier, limit + 1, multiplier))

def fibonacci(n):
    """Generate Fibonacci series up to nth term"""
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        result = [0, 1]
        for i in range(2, n):
            result.append(result[i-1] + result[i-2])
        return result

def top_spender():
    """Track expenses and identify top spender"""
    Rs = '\u20B9'
    num_entries = get_valid_int("How many entries are there? : ")
    print(f"Enter name and spent amount in {Rs} (format: 'name amount')")

    expenses = {}
    for i in range(num_entries):
        while True:
            entry = input(f"Entry {i+1}: ").strip()
            try:
                name, amount = entry.split()
                amount = int(amount)
                expenses[name] = expenses.get(name, 0) + amount
                break
            except ValueError:
                print("❌ Invalid format! Use: 'John 500'")

    # Find top spender
    top_name, top_amount = max(expenses.items(), key=lambda x: x[1])

    print("\n--- Expense Summary ---")
    for name, amount in sorted(expenses.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {Rs}{amount}")

    return f"\n🏆 Top Spender: {top_name} with {Rs}{top_amount}"

def display_menu():
    """Show main menu options"""
    print("="*60)
    print("📊 DATA ANALYSIS TOOLKIT")
    print("="*60)
    print("FF - First 5 characters")
    print("PL - Profit/Loss Calculator")
    print("PS - Perfect Squares Generator")
    print("XM - Multiples Finder")
    print("FS - Fibonacci Series")
    print("TS - Top Spender Tracker")
    print("-"*60)

def begin():
    """Main program loop"""
    display_menu()
    choice = input("Select an option: ").upper()

    Rs = '\u20B9'

    if choice == "FF":
        text = input("Enter text: ")
        print(f"Result: {first_five(text)}")

    elif choice == "PL":
        cost = get_valid_int(f"Cost price ({Rs}): ")
        selling = get_valid_int(f"Selling price ({Rs}): ")
        print(profit_loss(cost, selling))

    elif choice == "PS":
        limit = get_valid_int("Generate squares up to: ")
        print(f"Perfect squares: {perfect_squares(limit)}")

    elif choice == "XM":
        limit = get_valid_int("Find multiples up to: ")
        multiplier = get_valid_int("Multiplier: ")
        print(f"Multiples: {multiples(limit, multiplier)}")

    elif choice == "FS":
        terms = get_valid_int("Number of Fibonacci terms: ")
        print(f"Fibonacci: {fibonacci(terms)}")

    elif choice == "TS":
        print(top_spender())

    else:
        print("❌ Invalid option! Please try again.")

    # Ask to continue
    print("\n" + "-"*60)
    if input("Continue? (yes/no): ").lower() == "yes":
        begin()
    else:
        print("\n✨ Thank you for using Data Analysis Toolkit! ✨")

def main():
    """Entry point with error handling"""
    try:
        begin()
    except KeyboardInterrupt:
        print("\n\n👋 Program terminated by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please report this issue.")

if __name__ == "__main__":
    main()