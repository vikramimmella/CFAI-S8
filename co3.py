# CO3 - Constraint Satisfaction Based Recommendation
# Concepts Used:
# CSP
# Constraints
# Filtering
# Final Decision Making

from co1 import courses

print("FINAL COURSE RECOMMENDATION SYSTEM\n")

# User preferences
placement_importance = int(input("Placement importance (1-10): "))
interest_importance = int(input("Interest importance (1-10): "))
difficulty_preference = int(input("Preferred difficulty level (1-10): "))
max_credits = int(input("Maximum credits allowed: "))

valid_courses = []

print("\nAPPLYING CONSTRAINTS...\n")

# Constraint Satisfaction
for course in courses:

    # Constraint checking
    if course["credits"] <= max_credits:

        valid_courses.append(course)

        print(course["name"], "Accepted")
        print("Credits:", course["credits"])
        print()

    else:

        print(course["name"], "Rejected")
        print("Reason: Credits exceed limit")
        print()

# Final recommendation
best_course = None
best_score = -1

print("CALCULATING FINAL SCORES...\n")

for course in valid_courses:

    score = (
        placement_importance * course["placement"] +
        interest_importance * course["interest"] -
        abs(difficulty_preference - course["difficulty"])
    )

    print("Course:", course["name"])
    print("Final Score:", score)
    print()

    if score > best_score:
        best_score = score
        best_course = course

print("FINAL RECOMMENDED COURSE\n")

print("Course Name:", best_course["name"])
print("Best Score:", best_score)

print("\nReason:")

if best_course["placement"] >= 8:
    print("- High placement opportunities")

if best_course["interest"] >= 8:
    print("- Matches student interests")

if best_course["credits"] <= max_credits:
    print("- Fits within credit constraints")