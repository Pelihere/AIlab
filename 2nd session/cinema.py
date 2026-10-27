age = int(input("Enter your age: "))
day = input("Enter the day of the week: ").strip()

if age < 5:
    price = 0
elif age <= 12:
    price = 50000
elif age >= 60:
    price = 60000
else:
    price = 100000

if day == "سه‌شنبه" or day == "سه شنبه":
    price *= 0.8

if price == 0:
    print("ورود رایگان!")
else:
    print(f"قیمت بلیط: {price:.0f} تومان")