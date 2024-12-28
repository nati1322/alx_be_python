task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match priority:
      case "high":
          reminder_prefix = "**High priority:** "
      case "medium":
          reminder_prefix = "**Medium priority:** "
      case "low":
          reminder_prefix = "' is a low priority task. Consider completing it when you have free time."
      case _:
          reminder_prefix = "Invalid priority level. "
if time_bound == "yes":
    print("Reminder: '", task, "' is a ", reminder_prefix, "task that requires immediate attention today!")
else :
    print("Reminder: '", task, "' is a ", reminder_prefix, "task. Consider completing it when you have free time.")