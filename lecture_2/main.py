CURRENT_YEAR = 2025

def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Time traveler or something"

user_name = input("Enter your name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = CURRENT_YEAR - birth_year

hobbies = []
while True:
    hobby_input = input("Enter a hobby (type 'stop' to finish): ")
    if hobby_input.lower() == 'stop':
        break
    hobbies.append(hobby_input)

life_stage = generate_profile(current_age)

user_profile = {
    "user_name": user_name,
    "age": current_age,
    "hobbies": hobbies
}

print("\n--- Profile Summary ---")
print(f"Name: {user_profile['user_name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {life_stage}")

if not user_profile["hobbies"]:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile["hobbies"]:
        print(f"* {hobby}")
print("---")
