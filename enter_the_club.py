name = input("What is your name? ")
age = int(input("What is your age? "))
if age >= 18:
    print("You are welcome, " + name)
else:
    age_to_wait = 18 - age
    print(f"Sorry, see you in {age_to_wait} years")