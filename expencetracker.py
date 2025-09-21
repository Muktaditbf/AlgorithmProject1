# Expense Tracker with FUN + Bubble Sort 

expenses = []

while True:
    print("\nWhat do you want to do?")
    print("👉 Add(a)  👉 View(v)  👉 Sort(s)  👉 Total(t)  👉 Quit(q)")
    choice = input("Choose: ")

    if choice == "a":
        name = input("What did you buy? ")
        money = int(input("How much money? "))
        expenses.append((name, money))
        print("✅ Added:", name, "-", money, "💰")

    elif choice == "v":
        print("📒 Your expenses:")
        for name, money in expenses:
            print("•", name, ":", money, "💵")

    elif choice == "s":
        print("🔄 Sorting your expenses...")
        # Bubble sort (small to big)
        for i in range(len(expenses)):
            for j in range(0, len(expenses)-i-1):
                if expenses[j][1] > expenses[j+1][1]:
                    expenses[j], expenses[j+1] = expenses[j+1], expenses[j]
        print("🎯 Sorted (small → big):")
        for name, money in expenses:
            print("•", name, ":", money, "💵")

    elif choice == "t":
        total = 0
        for name, money in expenses:
            total += money
        print("💡 Total spent:", total, "💰")
        if total > 1000:
            print("😱 Whoa! You spent a lot!")
        else:
            print("🤑 Nice! You are saving money.")

    elif choice == "q":
        print("👋 Bye! Thanks for using Expense Tracker!")
        break

    else:
        print("⚠️ Wrong choice, try again!")
