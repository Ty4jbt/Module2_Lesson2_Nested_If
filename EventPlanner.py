# Task 1
attendees = int(input("Enter the number of attendees: "))

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2
attendees = int(input("Enter the number of attendees: "))

if attendees > 100:
    venue = "large hall"
    if attendees > 150:
        feature = "audio system"
    else:
        feature = "projector"
else:
    venue = "conference room"
    if attendees > 50:
        feature = "audio system"
    else:
        feature = "projector"

# Task 3
if attendees > 100:
    venue = "large hall"
    if attendees > 150:
        feature = "audio system"
    else:
        feature = "projector"
    food_preference = input("Would you like vegetarian or non-vegetarian food? ")
    if food_preference == "vegetarian":
        print("You should have Veggie Delight Caterers provide the meal!")
    else:
        print("You should have Gourmet Meals Cateres provide the meal!")
else:
    venue = "conference room"
    if attendees > 50:
        feature = "audio system"
    else:
        feature = "projector"
    food_preference = input("Would you like vegetarian or non-vegetarian food? ")
    if food_preference == "vegetarian":
        print("You should have Veggie Delight Caterers provide the meal!")
    else:
        print("You should have Gourmet Meals Cateres provide the meal!")