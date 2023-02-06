# This file will gather the data

import csv

# Define the chores list
chores = [
    "Cleaning the kitchen",
    "Vacuuming or sweeping floors",
    "Dusting and cleaning surfaces",
    "Doing laundry",
    "Cleaning bathrooms",
    "Taking out the trash and recycling",
    "Mowing the lawn or maintaining the garden",
    "Grocery shopping",
    "Cooking and meal preparation",
    "Ironing clothes",
    "Cleaning windows and mirrors",
    "Organizing and decluttering",
    "Sweeping the porch or walkways",
    "Cleaning the car(s)",
    "Pet care"
]

# Function to ask a family member about their preferences for each chore
def survey_family_member(name):
    member_preferences = []
    print(f"Surveying {name}:")
    for chore in chores:
        while True:
            try:
                importance = int(input(f"How important do you think {chore} is on a scale of 1 to 5? "))
                if importance < 1 or importance > 5:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
        while True:
            try:
                competence = int(input(f"How competent do you think you would be at {chore} on a scale of 1 to 5? "))
                if competence < 1 or competence > 5:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
        while True:
            try:
                comfort = int(input(f"How comfortable would you be with being responsible for {chore} on a scale of 1 to 5? "))
                if comfort < 1 or comfort > 5:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
        member_preferences.append([name, chore, importance, competence, comfort])
    return member_preferences

# Ask for each family member's name and preferences
header = ["Name", "Chore", "Importance", "Competence", "Comfort"]
all_preferences = []
while True:
    name = input("Enter the name of a family member (or press Enter to quit): ")
    if name == "":
        break
    member_preferences = survey_family_member(name)
    all_preferences += member_preferences

# Save the preferences to a CSV file
with open("family_preferences.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(all_preferences)

print("Preferences saved to family_preferences.csv")
