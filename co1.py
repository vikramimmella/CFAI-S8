# CO1 - Intelligent Agent Based Course Recommendation System

# Concepts Used:
# Agent Model (PEAS)
# State Representation
# Knowledge Representation
# Dataclass
# Lists, Dictionaries, Sets
# Trace Logging

from dataclasses import dataclass

print("INTELLIGENT AGENT BASED COURSE RECOMMENDATION\n")

# PEAS Model
print("PEAS MODEL")
print("Performance Measure : Recommend best course")
print("Environment         : Online Course Platform")
print("Actuators           : Display Recommended Course")
print("Sensors             : Student Preferences\n")


# State Representation
@dataclass
class StudentState:
    interest: str
    difficulty: int
    budget: int


# Knowledge Representation
courses = [

    {
        "name": "Artificial Intelligence",
        "interest": "AI",
        "difficulty": 8,
        "cost": 5000
    },

    {
        "name": "Data Science",
        "interest": "Data",
        "difficulty": 7,
        "cost": 4500
    },

    {
        "name": "Machine Learning",
        "interest": "AI",
        "difficulty": 9,
        "cost": 6000
    },

    {
        "name": "Web Development",
        "interest": "Web",
        "difficulty": 5,
        "cost": 3000
    }

]

# User Input
interest = input("Enter Interest (AI/Data/Web): ")
difficulty = int(input("Preferred Difficulty (1-10): "))
budget = int(input("Enter Budget: "))

# Initial State
state = StudentState(
    interest,
    difficulty,
    budget
)

print("\nSTATE CREATED")
print(state)

print("\nAGENT REASONING PROCESS\n")

recommended = []

visited = set()

for course in courses:

    print("Checking:", course["name"])

    # Action
    action = "Evaluate Course"

    # Transition Test
    if (
        course["interest"] == state.interest
        and course["difficulty"] <= state.difficulty
        and course["cost"] <= state.budget
    ):

        recommended.append(course)
        visited.add(course["name"])

        print("Action:", action)
        print("Result : Course Accepted\n")

    else:

        print("Action:", action)
        print("Result : Course Rejected\n")

# Goal Test
print("RECOMMENDED COURSES\n")

if len(recommended) > 0:

    for course in recommended:

        print("Course Name :", course["name"])
        print("Difficulty  :", course["difficulty"])
        print("Cost        :", course["cost"])
        print()

else:

    print("No Suitable Course Found")

print("VISITED STATES")
print(visited)