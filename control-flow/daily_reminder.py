task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"Reminder: '{task}' is a "

match priority.lower():
  case "high":
    reminder += "high priority task"
  case "medium":
    reminder += "medium priority task"
  case "low":
    reminder += "low priority task"
  case _:
    reminder += "task with invalid priority"

if time_bound == "yes":
  reminder += " that requires immediate attention today!"
else:
  reminder += ". Consider completing it when you have free time."

print(reminder)