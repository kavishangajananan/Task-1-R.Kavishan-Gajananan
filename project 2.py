# =========================================
# Expense Tracker Program
# DecodeLabs - Python Project 2
# =========================================

print("===================================")
print("       EXPENSE TRACKER SYSTEM      ")
print("===================================\n")

# Store total expense
total = 0

# Store highest expense
highest = 0

# Ask user how many expenses they want to enter
count = int(input("How many expenses do you want to enter? : "))

print()

# Loop for entering expenses
for i in range(count):

    print("Expense", i + 1)

    # Get expense amount from user
    expense = float(input("Enter expense amount: "))

    # Add expense to total
    total = total + expense

    # Check highest expense
    if expense > highest:
        highest = expense

    print()

# Calculate average expense
average = total / count

# Display final report
print("===================================")
print("         EXPENSE REPORT            ")
print("===================================")

print("Total Expenses Entered :", count)
print("Total Spent            :", total)
print("Average Expense        :", round(average, 2))
print("Highest Expense        :", highest)

print("===================================")
print("      THANK YOU FOR USING          ")
print("        EXPENSE TRACKER            ")
print("===================================")
