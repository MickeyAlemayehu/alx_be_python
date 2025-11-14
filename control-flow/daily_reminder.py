task = input("Enter a task description: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes/no): ").lower()

match priority:
    case "high":    
        if time_bound == "yes":
            print(f"Reminder: ''{task}'' is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be addressed within the next few days.")
        else:
            print(f"Note: '{task}' is a medium priority task. You can schedule it for later this week.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that can be scheduled for later this week.")    
        else:
            print(f"Note: '{task}' is a low priority task. Feel free to complete it at your convenience.")
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
