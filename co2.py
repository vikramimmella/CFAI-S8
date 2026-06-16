# CO2 - Search Based Course Selection
# Concepts Used:
# Search
# Heuristic Selection
# State Evaluation

from co1 import courses

print("SEARCHING BEST COURSE\n")

best_course = None
best_score = -1

# User preferences
placement_importance = int(input("Placement importance (1-10): "))
interest_importance = int(input("Interest importance (1-10): "))
difficulty_preference = int(input("Preferred difficulty level (1-10): "))

print("\nEvaluating Courses...\n")

for course in courses:

    # Heuristic score calculation
    score = (
        placement_importance * course["placement"] +
        interest_importance * course["interest"] -
        abs(difficulty_preference - course["difficulty"])
    )

    print("Checking:", course["name"])
    print("Placement:", course["placement"])
    print("Interest:", course["interest"])
    print("Difficulty:", course["difficulty"])
    print("Calculated Score:", score)
    print()

    # Best course selection
    if score > best_score:
        best_score = score
        best_course = course

print("BEST COURSE FOUND USING SEARCH\n")

print("Course Name:", best_course["name"])
print("Best Score:", best_score)