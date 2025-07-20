task = input("Enter your task: ").lower()
priority_level = input("Enter priority(high/medium/low: )").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority_level :
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else :
            print(f"{task} is a high priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires immediate attention today!")
        else :
            print(f"{task} is a medium priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes" :
            print(f"{task} is a low priority task that requires immediate attention today!")
        else :
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Unknown priority level entered. Please use high, medium or low.")