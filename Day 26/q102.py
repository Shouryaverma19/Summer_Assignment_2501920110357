age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    years_left = 18 - age
    print(f"You are not eligible to vote. You can vote after {years_left} years.")